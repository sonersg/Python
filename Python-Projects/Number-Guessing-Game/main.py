import random

min_number = 1
max_number = 100
answer = random.randint(min_number, max_number)
number_of_guesses = 0
is_running = True

print("\n\nPython Number Guessing Game\n\n")
print(f"Select a number between {min_number} and {max_number}\n\n")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        if guess < min_number or guess > max_number:
            print(f"{guess} is out of range!")
            print(f"Select a number between {min_number} and {max_number}\n\n")
            number_of_guesses += 1
        elif guess > answer:
            print("Too high!")
            number_of_guesses += 1
        elif guess < answer:
            print("Too low!")
            number_of_guesses += 1
        else:
            print(f"\n\nCorrect! The answer was {answer}")
            print(f"Number of guesses: {number_of_guesses}\n\n\n\n")
            is_running = False
    else:
        print(f"{guess} is not valid!")
        print(f"Select a number between {min_number} and {max_number}\n\n")


        