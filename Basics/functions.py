# Reusable block of code

def sum_num(a=0, b=0):
    if(a is not int or b is not int): return 0
    return a+b

total = sum_num("15",14)
print(total)

# asteriks (*) makes the type tuple
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Soen", "Soner")

def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_named_items(first = "Soen", second = "Soner")


