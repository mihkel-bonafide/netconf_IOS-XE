from ncclient import manager
import xmltodict
import xml.dom.minidom

"""
First successful get_config operation with ncclient! 
Worth exploring whether the solution to this whole fiasco is as simple/dumb as my dictionary
values not translating into these modules correctly whereas the global vars work just fuckin' fine.
Nonetheless, the netconf filter here works and THIS WORKING COPY SHOULD REMAIN UNTOUCHED! -MPG, 8.29.24

Explore further at: https://github.com/CiscoDevNet/dne-dna-code/blob/master/intro-mdp/netconf/get_interface_list.py
Also: https://developer.cisco.com/learning/modules/intro-device-level-interfaces/intro-netconf/walking-through-automating-your-network-with-netconf/

"""

HOST = "192.168.X.X"
PORT = "830"
USER = "XXX"
PW = "XXX"
LOOPBACK_ID = "01"
LOOPBACK_IP = "6.6.6.6/32"

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

def get_interfaces():
    with manager.connect(
        host=HOST, 
        port=PORT,
        username=USER,
        password=PW,
        hostkey_verify=False
    ) as miiihker:
        print("Sending a <get-config> operation to the device.\n")
        # Make a NETCONF <get-config> query using the filter
        netconf_reply = miiihker.get_config(source = 'running', filter = netconf_filter)
        print(f"Here is the raw data:")
        print()
        print(netconf_reply)
        print()
        print(f"Here is the same data formatted with xml.dom.minidom:")
        print()
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
        print()
        print(f"and here we're parsing the data into a Python dictionary with XMLtoDict:")
        opus = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        print(opus)
        print()
        print(f"parsing further...")
        print()
        interfaces = opus["interfaces"]["interface"]
        for interface in interfaces:
            print("Interface {} enabled status is {}".format(
                interface["name"],
                interface["enabled"]
            ))


if __name__ == '__main__': 
    get_interfaces() 