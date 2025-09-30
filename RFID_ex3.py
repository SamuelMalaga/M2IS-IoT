import serial
import time
import paho.mqtt.client as mqtt

IDS_IN_ROOM = []

def on_recieve_message(client, data, message):
    id = message.payload.decode("utf-8")
    print(f"Message recieved -> {id} ")
    print(f"Recieved ID -> {id}")
    IDS_IN_ROOM.append(id)

PortRF = serial.Serial('/dev/ttyAMA0',9600)

client = mqtt.Client()

client.connect('10.12.220.101',1883, 60)

client.on_message = on_recieve_message

client.loop_start()

client.subscribe('2IS/CardExercice')

try:

    while True:
        ID = ""
        read_byte = PortRF.read()
        if read_byte ==b"\x02":
            for i in range (0,12):
                read_byte=PortRF.read()
                ID += read_byte.decode('utf-8')

        if ID !="":
            print(f"Read ID -> {ID}")
            time.sleep(2)
            if ID in IDS_IN_ROOM:
                print("Hello you're allowed to exit")
                IDS_IN_ROOM.remove(ID)
                time.sleep(2)
            else:
                print(f"You'll never leave")
        


except KeyboardInterrupt:
    print("Disconnecting")
    client.loop_stop()
    client.disconnect()
