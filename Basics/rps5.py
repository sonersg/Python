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

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "You win! ✨😎✨"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win! ✨😎✨"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win! ✨😎✨"
            elif player == computer:
                return "Tie Game! 🤭"
            else:
                python_wins += 1
                return "Python wins! 🐍"
            
        print(decide_winner(player, computer))
        
        nonlocal game_count
        game_count += 1
        print("\nGame count: " + str(game_count))

        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

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

    return play_rps

rps()() # closure 
