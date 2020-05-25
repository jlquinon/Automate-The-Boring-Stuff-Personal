#! /usr/bin/env python3

import random, pyinputplus as pyip

COIN_FACE = {
        0 : 'tails',
        1 : 'heads'
    }

toss = COIN_FACE[random.randint(0, 1)]     # 0 is tails, 1 is heads

guess = pyip.inputChoice(choices=['heads', 'tails'], prompt="Guess the coin toss!\n")

if toss == guess:
    print('You got it!')
else:
    guess = pyip.inputChoice(choices=['heads', 'tails'], prompt="Nope! Guess again!\n")
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
