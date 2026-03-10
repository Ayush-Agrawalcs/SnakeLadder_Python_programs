import random
pos=0
print("Welcome to the Snake and Ladder Game!")
print("Single player at start position",pos)

def roll_dice():
    dice=random.randint(1,6)
    return dice
def choose_option(dice):
    option=random.randint(1,3)
    if(option==1):
        print("No move")
    elif(option==2):
        pos+=dice
    else:
        pos-=dice
        

