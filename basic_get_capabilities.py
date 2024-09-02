from ncclient import manager
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "192.168.x.x", "port": "830",
          "username": "XXX", "password": "XXX"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    # m.close_session()  # bad syntax, throws an error

