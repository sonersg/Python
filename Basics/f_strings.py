name = "Dave"
coins = 3

print("\n" + name + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left" %(name, coins)
print(message)

message = "\n{} has {} coins left".format(name, coins)
print(message)

message = "\n{1} has {0} coins left".format(name, coins)
print(message)

message = "\n{name} has {coins} coins left".format(name=name, coins=coins)
print(message)

player = {"name": "Dave", "coins": 3}

message = "\n{name} has {coins} coins left".format(**player)
print(message)

# F-STRINGS
message = f"\n{name} has {coins} coins left."
print(message)

message = f"\n{name} has {2 * 8} coins left."
print(message)

message = f"\n{name.lower()} has {coins} coins left."
print(message)

message = f"\n{player['name']} has {coins} coins left."
print(message)

# For more;
# https://www.w3schools.com/python/ref_string_format.asp
