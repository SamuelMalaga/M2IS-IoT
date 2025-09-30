import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


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


GAME_LEDS = [LED(26, "Red"), LED(24, "White"), LED(22, "Blue")]


def generate_sequence(round_number, LEDs):
    answer = ''
    for i in range(0, round_number):
        random_LED_number = random.randint(0, len(LEDs) - 1)
        led_to_light = LEDs[random_LED_number]
        led_to_light.light_up()
        #print(f"Showing {i} with the color -> {led_to_light.COLOR_NAME}")
        answer += led_to_light.COLOR_NAME[0]
    return answer


def check_answer(solution: str, input_str: str) -> bool:
    correct = False
    if solution.lower() == input_str.strip().lower():
        print("CORRECT ANSWER !!!!")
        correct = True
    else:
        print("Wrong answer :((")
    time.sleep(1)
    print("\033[H\033[J", end="")
    return correct


def init_game():
    round_num = 1
    display_rules()

    while True:
        print(f"Be prepared, this sequence will have a total of {round_num} blinks")
        time.sleep(1)

        answer = generate_sequence(round_num, GAME_LEDS)
        user_input = input("What is the sequence that was shown by the LEDs? \n")

        result = check_answer(answer, user_input)

        if result:
            round_num += 1
        else:
            break


def display_rules():
    print("Welcome to the super awesome Simon game \n")
    print("The answer should be input in a string-like format \n")
    print("'b' is for blue \n")
    print("'r' is for red \n")
    print("'w' is for white \n")
    print("Prepared??? \n")

    time.sleep(1)

    for i in range(5, 0, -1):
        print(f"Starting in {i} seconds")
        time.sleep(1)

    print("\033[H\033[J", end="")


if __name__ == '__main__':
    init_game()
    GPIO.cleanup()

