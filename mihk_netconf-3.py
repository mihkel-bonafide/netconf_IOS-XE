from ncclient import manager
import xml.dom.minidom
import xmltodict

"""
This code retrieves equivalent info to "R1# show interfaces GigabitEthernet2".
This is a proof-of-concept: "mihk_netconf-4.py" is going to take this a step 
further and ask the user which interface they wish to query, then apply an 
appropriate filter for the get request. 
MPG, 9.1.24


"""
router = {"host": "192.168.6.139", "port": "830",
          "username": "mihker", "password": "cisco$5446"}

netconf_filter = """
 <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""

# print(netconf_filter)
print('getting running config')

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # for capability in m.server_capabilities:
    #     print('*' * 50)
    #     print(capability)
        
    interface_netconf = m.get(netconf_filter)
    xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    print(xmlDom.toprettyxml(indent="  "))
    print(f"attempting to parse...")
    opus = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]
    # print(opus)
    interface_name = opus["name"]
    # print(interface_name)
    int_operational_status = opus["oper-status"]
    int_admin_status = opus["admin-status"]
    # print(int_operational_status)
    # print(int_admin_status)
    mac = opus["phys-address"]
    int_speed = int((opus["speed"])) / 1000000  # Mbps
    # print(mac)
    # print(int_speed)
    print(f"basic deets for {interface_name}: ")
    print(f"* MAC-address: {mac}")
    print(f"* operational status: {int_operational_status}")
    print(f"* admin status: {int_admin_status}")
    print(f"* interface speed: {int_speed} Mbps")



# m.close_session()  # throws error for some weird reason


