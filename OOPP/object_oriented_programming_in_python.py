# ##############################################
# OOPP: Object Oriented Programming in Python
# ##############################################

name = "Soner"
age = 99

# print(type(name))
# print(type(age))


class Dog:
    def __init__(self, name, breed, owner) -> None:
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof", self.name, self.breed)


class Owner:
    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number


owner = Owner("trump", "8765-8765")
dog1 = Dog("whoof", "kangal", owner)
# dog1.bark()
print(dog1.owner.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        self.age = 22
        print(
            f"Yo, i am a {self.age} yo boy, and my name is {self.name}. so abysmal to meet u"
        )


person1 = Person("Soner", 11)
person1.getName()
