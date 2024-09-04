import streamlit
import random
from random import randint
streamlit.title ("User Guessing Game")
guess_num = random.randint(1,100)
while True:
    entered_num = int(input('enter number: '))
    if entered_num > guess_num:
        print("Too high Guess, Try again!")
    elif entered_num < guess_num:
        print("Too low Guess, Try again!")
    else:
        print("Congratulations! You guessed the Correct Number")
