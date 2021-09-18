from pyModbusTCP import client
from pyModbusTCP.client import ModbusClient


client = ModbusClient(host="127.0.0.1",port=443)
client.open()

single_register = client.write_single_register(1,3)
client.close()