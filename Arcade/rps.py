# rock-paper-scissors

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

def rps(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        playerChoice = input(f"\n{name}, please enter ...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\n\n")

        pattern = r"^[1-3]$" 

        if re.match(pattern, playerChoice):
            player = int(playerChoice)
        else:
            play_rps()

        computer = int(random.choice("123"))

        print("")
        print(f"You chose {str(RPS(player)).replace('RPS.', '')}")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}")
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
                return f"Python wins! 🐍, {name} sucks!"
            
        print(decide_winner(player, computer))
        
        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {game_count}")

        print(f"{name}'s wins: {player_wins}")
        print(f"Python wins: {python_wins}")

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

    play_rps()

# rps()() # closure 

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description="Play rock-paper-scissors."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the player?"
    )

    args = parser.parse_args()

    rps(args.name)
