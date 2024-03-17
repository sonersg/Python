# Closure is a function having access to the scope of 
# its parent function after the parent function has returned.

def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game

# parent_function("Soner")()

soenr = parent_function("Soner")
soenr()
soenr()
soenr()
yavuz = parent_function("Yavuz")
soenr()
yavuz()
