from ncclient import manager
import xmltodict
import xml.dom.minidom

"""
Basic template for pulling raw XML data from a module; here ietf-interfaces
-MPG, 8.30.24
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
        netconf_reply = miiihker.get_config(source = 'running', filter=None)
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


if __name__ == '__main__': 
    get_interfaces() 