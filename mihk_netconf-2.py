from ncclient import manager
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "192.168.X.X", "port": "830",
          "username": "XXXXX", "password": "XXXXX"}

with manager.connect(host=mihk_router["host"], port=mihk_router["port"], username=mihk_router["username"], password=mihk_routerrouter["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)



