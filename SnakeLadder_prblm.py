import random
pos=0
pos1=0
print("Welcome to the Snake and Ladder Game!")
print("First player at start position",pos)
print("Second player at start position",pos1)
count=0
even=random.randint(0,1)
def roll_dice():
    dice=random.randint(1,6)
    return dice


def choose_option(dice):
    global pos
    global pos1
    option=random.randint(1,3)
    if(option==2):
        if(even%2==0):
            if(pos+dice<=100):
                pos+=dice
        else:
            if(pos1+dice<=100):
                pos1+=dice
        k=roll_dice()
        choose_option(k)

    elif(option==3):
             if(even%2==0):
                  pos-=dice
                  if(pos<0):
                      pos=0
             else:
                    pos1-=dice
                    if(pos1<0):
                        pos1=0
    print(pos)
    if(even%2==0):
        return pos
    else:
         return pos1

while(pos<100 and pos1<100):
    dice=roll_dice()
    if(even%2==0):
         pos=choose_option(dice)
    else:
       pos1=choose_option(dice)
   
    count+=1
    even+=1
if(pos>=100):
    print("Player1 win")
else:    
     print("Player2 win")

print("Total no. of dice role: ",count)