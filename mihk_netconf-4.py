from ncclient import manager
from netconf_filters import named_interface_filter as muh_filter
import xml.dom.minidom
import xmltodict

"""
This code retrieves equivalent info to "R1# show interfaces GigabitEthernet2" for
a user-selected interface on the target-device "router". 
This specific version includes various code used for testing - the file "mihk_netconf-4p.py" 
contains the 'production' version of this same file. 
The next iteration of this code will perform the same operation but will query the target 
device for interface names (rather than hard-coding it).
MPG, 9.2.24

"""
router = {"host": "192.168.X.X", "port": "830",
          "username": "XXXXX", "password": "XXXXX"}


with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # for capability in m.server_capabilities:
    #     print('*' * 50)
    #     print(capability)
    
    netconf_filter = muh_filter()
    # print(netconf_filter)
    print('getting running config')
    interface_netconf = m.get(netconf_filter)
    # xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    # print(xmlDom.toprettyxml(indent="  "))
    # print()
    # print(f"parsing...parsing...")
    print()
    opus = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]
    # # print(opus)
    interface_name = opus["name"]
    # # print(interface_name)
    int_operational_status = opus["oper-status"]
    int_admin_status = opus["admin-status"]
    # # print(int_operational_status)
    # # print(int_admin_status)
    mac = opus["phys-address"]
    int_speed = int((opus["speed"])) / 1000000  # Mbps
    # # print(mac)
    # # print(int_speed)
    print(f"basic deets for {interface_name}: ")
    print(f"* MAC-address: {mac}")
    print(f"* operational status: {int_operational_status}")
    print(f"* admin status: {int_admin_status}")
    print(f"* interface speed: {int_speed} Mbps")



# m.close_session()  # throws error for some weird reason


# if __name__ == '__main__': 
#     get_interfaces() 