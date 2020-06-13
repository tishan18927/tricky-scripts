import time
import random
from pynput.keyboard import Key, Controller

"Once I wanted to add 10K comments on a fb post"

keyboard = Controller()  # Create the controller

#This function isnt used
def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0, 2)  # Generate a random number between 0 and 10
        time.sleep(delay)  # Sleep for the amount of seconds generated
    keyboard.press(Key.enter)

n = 0
time.sleep(10)
while(n < 10000):
    keyboard.type("Some text here")
    keyboard.press(Key.enter)
    time.sleep(random.uniform(0, 2))