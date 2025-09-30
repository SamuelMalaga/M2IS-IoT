import time
import paho.mqtt.client as mqtt


def run_message_loop(client,channel_name):
	print("Initializing listener")

	while True:

		message = input("Write the input > ")
		
		

		if message.lower().strip() == "exit":
			print("Disconnecting")
			client.loop_stop()
			client.disconnect()
			break

		client.publish(channel_name,message)

if __name__ == '__main__':
	client = mqtt.Client()
	client.connect('10.162.244.206',1883,60)
	client.loop_start()
	run_message_loop(client,"test")


