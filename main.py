
from re import I
from turtle import right

print()

print('''  *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
 ''')
print()

print("Welcome to the Tresure Island")

user = input("Do you want to find the tresure? yes/no\n").lower()

if user == "yes":
    print("Let's start the adventure!")
    answer = input("Do you want move left or right?\n").lower()
    
    if answer == "right":
        print("You can see the palm tree\n")
        answer = input("Where you want to go? left or right\n").lower()

        if answer == "right":
            print("Move forward!")

            answer = input("Where you want to go? forward or behind\n").lower()

            if answer == "forward":

              door = input("Choose a door! yellow, blue , red\n").lower()

              if door == "yellow":

                print("You win!")

              elif door == "blue" or door == "red":

                print("So close! Game Over!")
      
    elif answer == "left":
        print("Game Over!!")
             
else:
    print("Game Over!")