

import os

# r = read
# a = append
# w = write
# x = create

# read - error if it doesn't exist
f = open("names.txt")
print(f.read())
print(f.read(5))

print(f.readline())
print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("nane_list.txt")
    print(f.read())
except:
    print("The file may not exist.")
finally:
    f.close()



# append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("\nKyle")
f.close()
f = open("names.txt")
print(f.read())
f.close()



# write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context.")
f.close()
f = open("context.txt")
print(f.read())
f.close()



# two ways to create a file
# Opens a file for writing and creates the file if it doesn't exist.
f = open("new_context.txt", "w")
f.close()

# creates the file but returnes an error if it already exists.
if not os.path.exists("nnn.txt"):
    f = open("nnn.txt", "x")
    f.close()



# delete a file
if os.path.exists("nnn.txt"):
    os.remove("nnn.txt")
else:
    print("The file u try to delete doesn't exist!")



# with keyword
with open("more_names.txt") as f:
    content = f.read()
with open("names.txt", "w") as f:
    f.write(content)

