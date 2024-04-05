

class CustomError(Exception):
    pass

x = 1
try:
    raise CustomError("This is CustomError!")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined")
except ZeroDivisionError:
    print("Do not divide by zero.")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally:
    print("Ama print with or without an error!")
