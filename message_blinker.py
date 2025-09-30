import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GLOBAL_MESSAGE_COUNT = 0

class LED:
    def __init__(self, BOARD_NUM, COLOR_NAME):
        self.BOARD_NUM = BOARD_NUM
        self.COLOR_NAME = COLOR_NAME

    def light_up(self, SLEEP_BETWEEN=2, SLEEP_AFTER=1):
        GPIO.output(self.BOARD_NUM, GPIO.HIGH)
        time.sleep(SLEEP_BETWEEN)
        GPIO.output(self.BOARD_NUM, GPIO.LOW)
        time.sleep(SLEEP_AFTER)

    def __str__(self):
        return self.COLOR_NAME


LED1 = LED(22,"Red")
LED2 = LED(24,"white")

MESSAGE_QUEUE = []

def on_message_recieve(client, data, message):
    MESSAGE_QUEUE.append(message)
    global GLOBAL_MESSAGE_COUNT

    GLOBAL_MESSAGE_COUNT = GLOBAL_MESSAGE_COUNT + 1
    print("Recieved -> {} on topic -> | {}".format(str(message.payload), message.topic))


client = mqtt.Client()

client.connect('10.162.244.206',1883,60)

client.on_message = on_message_recieve

client.subscribe('test', qos=0)

client.loop_start()

queue_size = 0

OLD_MESSAGE_COUNT = GLOBAL_MESSAGE_COUNT

try:

    # while True:
    #     time.sleep(5)
    #     if len(MESSAGE_QUEUE) != queue_size:
    #         print(f"Recieved {len(MESSAGE_QUEUE) - queue_size} messages in the last 5 seconds")
    #         for message in MESSAGE_QUEUE:
    #             MESSAGE_QUEUE.pop()
    #             LED1.light_up(0.5,0.5)
    while True:
        time.sleep(5)
        new_messages = GLOBAL_MESSAGE_COUNT - OLD_MESSAGE_COUNT
        if new_messages != 0:
            print(f"Recieved {new_messages} messages in the last 5 seconds")
            for _ in range(new_messages):
                if _ % 2 ==0:
                    LED1.light_up(0.5,0.5)
                else:
                    LED2.light_up(0.5,0.5)
        else:
            print("No new messages in the last 5 seconds")
        
        GLOBAL_MESSAGE_COUNT = 0


except KeyboardInterrupt:

    print("\n disconnecting")

    GPIO.cleanup()

    client.loop_stop()

    client.disconnect()



