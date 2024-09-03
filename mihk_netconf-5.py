from ncclient import manager
import xmltodict

"""
This script queries a target device for its interfaces (up or down) then passes the 
interface-name into a netconf filter which can then query that interface for further 
details (everything from "show ip interfaces" but I'm only printing key details).
"""

router = {"host": "XXX", "port": "830",
          "username": "XXX", "password": "XXX"}

def get_interface_names(): 
    # The filter below allows you to enumerate through a target device's interface names
    # status (enabled, disabled). For our purposes, we're pulling interface names so we 
    # can use them for a subsequent RPC. 
    netconf_filter = """
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface></interface>
        </interfaces>
        </filter>    """
    # define "m"
    with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
        netconf_reply = m.get_config(source = 'running', filter = netconf_filter)
        py_dict = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        interfaces = py_dict["interfaces"]["interface"]  # parsing operation
        for interface in interfaces:
                opus = interface["name"]
                # print(opus)
                named_interface_filter(opus)

def named_interface_filter(opus):  # check out f""" from the line below!! :O 
    netconf_filter = f"""
      <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
            <name>{opus}</name>
            </interface>
        </interfaces>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
            <name>{opus}</name>
            </interface>
        </interfaces-state>
    </filter>
    """
    # print(netconf_filter)
    interface_data(netconf_filter)

def interface_data(netconf_filter): 
     with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
          target_interface = m.get(netconf_filter)
          opus = xmltodict.parse(target_interface.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]
          interface_name = opus["name"]
          int_operational_status = opus["oper-status"]
          int_admin_status = opus["admin-status"]
          mac = opus["phys-address"]
          int_speed = int((opus["speed"])) / 1000000  # Mbps
          print(f"basic deets for {interface_name}: ")
          print("@#$%" * 20)
          print(f"* MAC-address: {mac}")
          print(f"* operational status: {int_operational_status}")
          print(f"* admin status: {int_admin_status}")
          print(f"* interface speed: {int_speed} Mbps")
          print("****************************************")
          
def main():
    program_start = ""
    print(f"Please verify the login-credits at the top of this script.")
    print(f"When you're ready, type 'y' or 'yes' to scan the interfaces of the selected remote device.")
    program_start == "y"
    program_start = input(f"Begin? [yes/no]: ")
    if program_start.lower() == "y" or "yes":
         get_interface_names()
    else: 
         print(f"program aborted.")

main() 