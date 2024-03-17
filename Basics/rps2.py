# rock-paper-scissors

import sys
import random
import re
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
    
play_again = True

while play_again:
    playerChoice = input("\nEnter ...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\n\n")

    pattern = r"^[1-3]$" 

    if re.match(pattern, playerChoice):
        player = int(playerChoice)
    else:
        sys.exit("You must enter 1, 2 or 3.")

    computer = int(random.choice("123"))

    print("")
    print("You chose " + str(RPS(player)).replace("RPS.", ""))
    print("Python chose " + str(RPS(computer)).replace("RPS.", ""))
    print("")

    if player == 1 and computer == 3:
        print("You win! ✨😎✨")
    elif player == 2 and computer == 1:
        print("You win! ✨😎✨")
    elif player == 3 and computer == 2:
        print("You win! ✨😎✨")
    elif player == computer:
        print("Tie Game! 🤭")
    else:
        print("Python wins! 🐍")

    choice = input("\nPlay again? \ny for yes \n\n")
    if choice.lower() == "y":
        continue
    else:
        print("🎉 🎉 🎉 🎉 🎉 🎉 🎉")
        print("Thank you for playing!")
        play_again = False
        
sys.exit("Bye! 👋")
