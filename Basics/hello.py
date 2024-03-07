greeting = "Hello Python"
print(greeting) # comment

3+3
greeting

print(3**2) # 2 power of 3

a = True
b = False

print(a or b)
print(a and b)

# IF STATEMENT

i = 2

if i > 5:
    print("i > 5")
else:
    print("i < 5")

#TERNARY OPERATOR
print("with ternary operator")
    
print("i > 5") if i > 5 else print("i < 5")

############## STRING METHODS #############

#MULTILINE
multiline = '''
        Hello Python!   

                His name is NOT
hairy potter
'''

print(multiline)
print(multiline.title())
print(multiline.replace(" ", "*"))

print(len(multiline)) #length

print(multiline.strip()) #remove white spaces .trim()
print(multiline.lstrip()) #remove white spaces from left
print(multiline.rstrip()) #remove white spaces from right

t = "menü"
print(t.upper().center(20, "="))
print("Çay".ljust(16, ".") + "1₺".rjust(4, " "))
print("Simit".ljust(16, ".") + "2₺".rjust(4, " "))
print("Peynir".ljust(16, ".") + "2₺".rjust(4, " "))

print("")

# STRING INDEX VALUES
ben =  "Soner"
ben = str("Soner")
print(ben[1])
print(ben[-1])
print(ben[0:-1])
print(ben[0:])

# COMPLEX TYPE
comp_number = 3+5j
print(type(comp_number))
print(comp_number.real)
print(comp_number.imag)

# MATH LIBRARY
import math

print(abs(-45))
print(round(3.3))

print(math.pi)
print(math.sqrt(25))
print(math.ceil(3.3))
print(math.floor(3.3))

# CASTING A STRING TO A NUMBER
zip_code = "69500"
zip_value = int(zip_code)
print(type(zip_value))

#USER INPUT
userInput = input("input an input 🤭 \n")
print(userInput)
print(type(userInput))

