import random
from items import hidden_things
import string


def get_item_list():
    thing = random.choice(hidden_things)
    return thing

def whats_behind_my_back():
    thing = get_item_list
    guess = 0
    max_guess = 3

    while guess < max_guess:
        user_guess = input('so, what is behind my back?  ')
        if user_guess == thing:
            print('You are a gifted fellow!!!!')

        else:
            print('Come on fam! Try again!!!')
            guess += 1


    if guess == max_guess:
         print('You used all your guess bro!')

    print('Thanks for playing.')


whats_behind_my_back()

