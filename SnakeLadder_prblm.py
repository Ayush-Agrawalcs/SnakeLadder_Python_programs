import random
pos=0
print("Welcome to the Snake and Ladder Game!")
print("Single player at start position",pos)

def roll_dice():
    dice=random.randint(1,6)
    return dice
