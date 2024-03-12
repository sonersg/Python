# Dictionaries => key-value paires, similar to objects in js

band = {
    "id": "sodsa",
    "name": "Soner"
}

band2 = dict(id="kdfkl", name="Güçlü")

print(band)
print(band2)
print(type(band2))
print(len(band2))

# access items
print(band["id"])
print(band.get("id"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list key-values pairs as tuples
print(band.items())

# verify a key exists
print("id" in band)    # True
print("Soner" in band) # False

# change values
band["id"] = "1346"
band.update({"":""})
print(band)

# remove items
print(band.pop(""))
print(band)
band["name"] = "Hakan"
print(band)
print(band.popitem()) # tuple
print(band)

# delete and clear
band["name"] = "Furkan"
del band["id"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries
band2 = band.copy()
band2["drums"] = "Soenr"
print(band2)
print(band)

band3 = dict(band)
print(band3)

band2 = band #creates a reference
band2["drums"] = "Soenr"
print(band)

