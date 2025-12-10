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

# 2. Via Python Properties

print("\nVia Python Properties:\n")


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
