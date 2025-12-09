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

############################################
# Accessing and modifying data:
############################################
# 1. The traditional, java way: make the data private and use getters and setters;

from datetime import datetime


class Userr:
    def __init__(self, username, email) -> None:
        self.username = username
        # self._email = email
        self.__email = email

        # One underscore -> protected, can be accessed outside of the class
        # Double underscores, name mangled -> private, can't be accessed

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email


user1 = Userr("Soner", "kdsakfds@fdklskf.io")
print(user1.get_email())

user1.set_email(("sonersg@outlook.com"))
print(user1.get_email())

# 2. Properties
print("Properties")


class User:
    def __init__(self, username, email) -> None:
        self.username = username
        self._email = email

    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("Soner", "kdsakfds@fdklskf.io")
print(user1.email)
