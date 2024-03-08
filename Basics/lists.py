

users = ["Soner", "Seiim", "Yavuz"]
data = list(["Soner", 26, True]) # with constructor
emptyList = []

print(users[0])
print(users[-2])
print(users[0:2])
print(users[0:])
print(users[-3:-1])
print(users.index("Soner"))
print("Soner" in emptyList)
print(len(data))

# push new items
users.append("Selahaddin")
users += ["Vahid"]
users.extend(["Kerim", "Severim"])
print(users)

users.insert(0, "Güçlü")
print(users)

users[2:2] = ["iki", "iki"]
print(users)

users[1:3] = ["bir", "üç"]
print(users)

# delete item
users.remove("Vahid")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

newList = [1, 2]
del newList

data.clear()
print("data", data)

# sort
nums = [2, 5, 54, 65, 9]

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))



# TUPLES
# Tuples are very much like arrays, links 
# except order and type does not change.

myTuple = (1, 4, 2, 8)          # packing
anotherTuple = tuple(("Soner", 26, False))

print(myTuple)
print(anotherTuple)

newList2 = list(myTuple)
newList2.append("Osman")
newTuple = tuple(newList2)
print(newTuple)

(one, *two, hey) = anotherTuple #unpacking
# ig unpacking is similar to destructuring in js
print(one)
print(two)
print(hey)


