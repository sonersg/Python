# use "global" keyword to modify a global variable
# use "nonlocal" keyword to modify a parent variable
# avoid using global variables

name = "Soenr"
count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count) #2

    def greeting(name):
        nonlocal color
        print(color) # blue
        color = "red"
        print(color) # red
        print(name) # Soner

    greeting("Soner")

another()

