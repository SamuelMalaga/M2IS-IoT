import time
import paho.mqtt.client as mqtt

MESSAGE_QUEUE = []

def on_message_recieve(client, data, message):
    MESSAGE_QUEUE.append()
    print("Recieved -> {} on topic -> | {}".format(str(message.payload), message.topic))



def run_listening_loop(client, channel_name):
    client.subscribe(channel_name, qos=0)
    print("Listening messages from {}".format(channel_name))
    while True:
        action = input("action >")

        if action.lower().strip() == "exit":
            print("Disconnecting")
            client.loop_stop()
            client.disconnect()
            time.sleep(1)
            print("\033[H\033[J", end="")
            break





if __name__=='__main__':
    client = mqtt.Client()
    client.connect('10.162.244.206',1883,60)
    client.on_message = on_message_recieve
    client.loop_start()
    run_listening_loop(client, "test")
