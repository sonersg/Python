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
    
game_count = 0

def play_rps():

    playerChoice = input("\nEnter ...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\n\n")

    pattern = r"^[1-3]$" 

    if re.match(pattern, playerChoice):
        player = int(playerChoice)
    else:
        play_rps()

    computer = int(random.choice("123"))

    print("")
    print("You chose " + str(RPS(player)).replace("RPS.", ""))
    print("Python chose " + str(RPS(computer)).replace("RPS.", ""))
    print("")

    
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "You win! ✨😎✨"
        elif player == 2 and computer == 1:
            return "You win! ✨😎✨"
        elif player == 3 and computer == 2:
            return "You win! ✨😎✨"
        elif player == computer:
            return "Tie Game! 🤭"
        else:
            return "Python wins! 🐍"
        
    print(decide_winner(player, computer))
    
    global game_count
    game_count += 1
    print("\nGame count: " + str(game_count))

    while True:
        choice = input("\nPlay again? \ny for yes \nq to quit \n\n")
        if choice.lower() not in ["y", "q"]:
            continue
        else:
            break
        
    if choice.lower() == "y":
        play_rps()
    else:
        print("🎉 🎉 🎉 🎉 🎉 🎉 🎉")
        print("Thank you for playing!")
        sys.exit("Bye! 👋")
        
play_rps()

