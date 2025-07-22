import random

welcome_string = '''
**************************************
***********   HANGMAN   **************
**************************************
'''

hangman_art = (
    ("      ",
     "      ",
     "      "),
    ("  o   ",
     "      ",
     "      "),
    ("  o   ",
     "  |   ",
     "      "),
    ("  o   ",
     "  |\\  ",
     "      "),
    ("  o   ",
     " /|   ",
     "      "),
    ("  o   ",
     " /|\\ ",
     "   \\ "),
    ("  o   ",
     " /|\\ ",
     " / \\ ")
              )

answer = "Sonerr".lower()
hint = list("_" * len(answer))

# main function
def main():
    print(f"\n\n{welcome_string}\n")

    while True:
        inpt = input("Press enter to play, q to quit: ")
        if inpt.lower() == "q": break
        start(answer)
    print(welcome_string ,"\nThanks for playing! 👋")

# display_man function
def display_man(wrong_guesses):
    print(wrong_guesses)
    for line in hangman_art[wrong_guesses]:
        print(line)

# display_hint function
def display_hint(guess):
    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                hint[i] = guess
    print()
    for char in hint:
        print(char+" ", end="")
    print("\n\n")

# display_answer function
def display_answer(answer):
    print()
    for char in answer:
        print(char+" ", end="")
    print("\n\n")

def start(answer):
    guessed_chars = []
    wrong_guesses = 0

    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or len(guess) == 0: continue
        print(guessed_chars)
        if guess not in answer and guess not in guessed_chars:
            wrong_guesses += 1
        guessed_chars.append(guess)
        display_man(wrong_guesses)
        display_hint(guess)
        if wrong_guesses >= 6:
            print("You lost! 🤷‍♂️")
            display_answer(answer)
            break
        if (set(answer).issubset(guessed_chars)):
            print("You won! 🥳")
            break

if __name__ == "__main__":
    main()
    