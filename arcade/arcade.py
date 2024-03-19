

from rps import rps
from guess_num import play

def hello(name):

    print(f"\nHello {name}! Welcome to the Arcade 🤭")
    
    while True:
        inpt = input(f"\nPlease choose a game...\n\n1 = Rock Paper Scissors\n2 = Guess My Number \n\nOr press 'X' to exit. \n\n")

        if inpt == "1":
            rps(name)
        elif inpt == "2":
            play(name)
        elif inpt == "x" or inpt == "X":
            print(f"Bye {name}! 👋 ")
            break

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of the player?"
    )

    args = parser.parse_args()

    hello(args.name)
