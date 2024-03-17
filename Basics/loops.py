
# WHILE LOOPS
value = 0
while value < 10:
    print(value)
    if value == 5:
        break
    value += 1

print("continue")
value = 0
while value < 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now " + str(value))

print("Value is now " + str(value))

# FOR LOOPS
names = ["Emre", "Can", "Bilge", "Bilgi", "Belge"]
for name in names:
    print(name)

for x in "Mississippi":
    print(x)

for x in range(3):
    print(x)
for x in range(1,3):
    print(x)
for x in range(0,30,2):
    print(x)
else:
    print("Glad that\'s over!")
