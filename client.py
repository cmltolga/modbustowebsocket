import asyncio
import datetime
import random
import websockets
from pyModbusTCP import client
from pyModbusTCP.client import ModbusClient
from time import sleep


async def time(websocket, path):
    
    try:
        client = ModbusClient(host="127.0.0.1",port=443)
        client.open()
        initial_register_value =[0,0,0,0,0,0]
        registers_value = client.read_holding_registers(0,6)
        for count in range(0,6):
            sleep(1)
            print(str(registers_value[count]))
            if initial_register_value[count]!=registers_value[count]:
                await websocket.send(str(count+1) +". register changed to "+ str(registers_value[count]))
                print(str(initial_register_value))
                initial_register_value[count] = registers_value[count]
    except:
        client.close()
    
start_server = websockets.serve(time,"127.0.0.1", 80)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()