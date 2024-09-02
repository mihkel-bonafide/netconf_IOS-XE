from ncclient import manager
# import logging
# logging.basicConfig(level=logging.DEBUG)

mihk_router = {"host": "192.168.6.135", "port": "830",
          "username": "mihker", "password": "cisco"}

with manager.connect(host=router["host"], port=mihk_router["port"], username=mihk_router["username"], password=mihk_routerrouter["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)



