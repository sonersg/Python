

import random as rnd

def play(name="Player"):

    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_guess_num(playerChoice):
        nonlocal name
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins
        
        num = rnd.choice("123")

        if num != playerChoice:
            computer_wins += 1
            print(f"Sorry {name}, you lost 😭")
            print(f"I was thinking {num}, you guessed {playerChoice}")
        elif num == playerChoice:
            player_wins += 1
            print(f"{name}, you won 😎")
            print(f"I was thinking {num}, you guessed {playerChoice}")

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"Success: {(player_wins / game_count) * 100} %")
        print(f"{name}'s wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
    

    while True:
        playerChoice = input(f"\n\n{name}, press... \n1, 2 or 3 to guess my number, \nx to exit. \n\n")

        if playerChoice == "1" or playerChoice == "2" or playerChoice == "3":
            play_guess_num(playerChoice)
        elif playerChoice == "x" or playerChoice == "X":
            print(f"Bye {name}! 👋 ")
            break
    

if __name__ == "__main__":
    play("Soenr")
