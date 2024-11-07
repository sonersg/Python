

# List [] : mutable, most flexible
# Set {} : mutable (add, remove), unordered, no duplicates
# Tuple () : immutable, faster

### LISTS
# animals = ["dog", "marmot", "wolf"]
# animals[0] = "wolf"
# animals.append("bird")
# animals.remove("bird")
# animals.clear()


### SETS
# animals = {"dog", "marmot", "wolf", "marmot"}
# animals.add("wolf")
# animals.clear()

### TUPLES
animals = ("dog", "marmot", "wolf", "marmot")

for item in animals:
    print(f"{item} ", end="")

