import time
import random



class LED:
    def __init__(self, BOARD_NUM, COLOR_NAME):
        self.BOARD_NUM = BOARD_NUM
        self.COLOR_NAME = COLOR_NAME
    
    def light_up(self, SLEEP_BETWEEN = 2, SLEEP_AFTER=1):
        print(f"Light on for {self.COLOR_NAME}")
        time.sleep(SLEEP_BETWEEN)
        print(f"Light off for {self.COLOR_NAME}")
        time.sleep(SLEEP_AFTER)
        pass

    def __str__(self):
        return self.COLOR_NAME


GAME_LEDS = [LED(1, "Red"), LED(2, "White"), LED(3, "Blue")]


def generate_sequence(round_number, LEDs:list[LED]):

    answer = ''

    for i in range(0,round_number):
        random_LED_number = random.randint(0,len(LEDs)-1)
        led_to_light = LEDs[random_LED_number]
        led_to_light.light_up(0,0)
        print(f"Showing {i} with the color -> {led_to_light.COLOR_NAME}")
        answer+=led_to_light.COLOR_NAME[0]

    return answer

def check_answer(solution:str, input:str) -> bool:
    correct = False
    if solution.lower() == input.strip().lower():
        print("CORRECT ANSWER !!!!")
        correct = True
    else:
        print("Wrong answer :((")
    time.sleep(1)
    print("\033[H\033[J", end="")
    return correct
    

def init_game():

    round = 1

    display_rules()

    while True:
        
        print(f"Be prepared, this sequence will have a total of {round} blinks")

        time.sleep(1)

        answer = generate_sequence(round, GAME_LEDS)

        user_input = input("What are the sequence that was showed by the LED's? \n")

        result = check_answer(answer, user_input)

        if result:
            round +=1
        else:
            break
        

def display_rules():

    print("Welcome to the super awesome simon game \n")

    print("The answer shouls be inputed in a string-like format \n")

    print("'b' is por blue \n")

    print("'r' is por red \n")

    print("'w' is por white \n")

    print("Prepared??? \n")

    time.sleep(1)

    for i in range(5,0,-1):
        
        print(f"Starting in {i} seconds")
        time.sleep(1)

    print("\033[H\033[J", end="")

if __name__ == '__main__':
    init_game()