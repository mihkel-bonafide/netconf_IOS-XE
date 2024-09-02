
"""
This file holds various NETCONF filters (for testing purposes)
"""

def named_interface_filter():
    print(f"1. Interface: GigabitEthernet1")
    print(f"2. Interface: GigabitEthernet2")
    print(f"3. Interface: GigabitEthernet3")
    print(f"4. Interface: GigabitEthernet4")
    print(f"(Ideally here I'd like to have a module that pulls interface names from the target device...)")
    chosen_filter = int(input("Please select an interface: "))
    if chosen_filter == 1:
            chosen_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        <name>GigabitEthernet1</name>
        </interface>
    </interfaces-state>
    </filter>
    """
            return chosen_filter
    elif chosen_filter == 2:
          chosen_filter = """
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
          return chosen_filter
    elif chosen_filter == 3:
          chosen_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        <name>GigabitEthernet3</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        <name>GigabitEthernet3</name>
        </interface>
    </interfaces-state>
    </filter>
    """
          return chosen_filter
    elif chosen_filter == 4: 
          chosen_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        <name>GigabitEthernet4</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        <name>GigabitEthernet4</name>
        </interface>
    </interfaces-state>
    </filter>
    """
          return chosen_filter
    else:
          print(f"Invalid option")
          
# def main():
#       meeker = named_interface_filter()
#       print(meeker)

# main() 
