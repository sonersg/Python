import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
charsList = list(chars)
key = charsList.copy()

random.shuffle(key)

# print(f"chars: {charsList}")
# print(f"key  : {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = charsList.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message : {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to decrypt : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += charsList[index]

print(f"encrypted message : {cipher_text}")
print(f"original message : {plain_text}")
