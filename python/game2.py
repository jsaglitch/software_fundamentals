#game2.py

import os 
from random import randint
i=0
lives = 3 
status = True
intentos_totales =0
victorias =0
derrotas= 0

def roll_dice():
    dice1 =randint(1,6)
    dice2 =randint(1,6)
    return dice1,dice2
# print (roll_dice())

while True :
    key= input ("Press any Key to roll dices : ")
    dices= roll_dice()
    print(f"Dice 1 : {dices [0]}")
    print(f"Dice 2 : {dices [1]}")
    if(dices[0]+dices[1]) % 2 ==0:
        lives +=1
    else:
        lives -=1
        print("Lives:",lives)
    
    if dices[0] == 6 and dices[1] == 6: 
        print("YOU WIN")
        os.system("pause")
        break
    if lives == 0:
        print("GAME OVER")
        break
    for _ in range(i+1):
        intentos_totales +=1
        if intentos_totales== "jugadas":
            victorias +=1
        else:
            derrotas +=1
    print(f"intentos totaes:{intentos_totales}")
    print(f"victorias {victorias}")
    print(f"derrotas {derrotas}")
