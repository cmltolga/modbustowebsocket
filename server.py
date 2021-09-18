from select import error
from pyModbusTCP import server
from pyModbusTCP.server import ModbusServer,DataBank
from time import sleep
from random import uniform

server = ModbusServer("127.0.0.1",443,no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state =[0]
    while True:
        continue
except OSError in error:
    print("Shutdown Server ..."+str(error))
    server.stop()
    print("Server offline...")