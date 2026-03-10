import random
pos=0
print("Welcome to the Snake and Ladder Game!")
print("Single player at start position",pos)

def roll_dice():
    dice=random.randint(1,6)
    return dice
def choose_option(dice):
    global pos
    option=random.randint(1,3)
    if(option==2):
        pos+=dice
    elif(option==3):
        pos-=dice
        if(pos<0):
            pos=0
    return pos

while(pos<100):
    dice=roll_dice()
    pos=choose_option(dice)

if(pos>=100):
    print("Player1 win")
   
        

