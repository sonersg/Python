# List [] : mutable, most flexible
# Tuple () : immutable, faster
# Set {} : mutable (add, remove), unordered, no duplicates

### LISTS
# animals = ["dog", "marmot", "wolf"]
# animals[0] = "wolf"
# animals.append("bird")
# animals.remove("bird")
# animals.clear()

### TUPLES
# animals = ("dog", "marmot", "wolf", "marmot")

### SETS
animals = {"dog", "marmot", "wolf", "marmot"}
animals.add("wolf")
animals.clear()

for item in animals:
    print(f"{item} ", end="")
