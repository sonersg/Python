# Protected, private instance attributes and methods

# One underscore -> protected, can be accessed outside of the class
# Double underscores, name mangled -> private, can't be accessed


from datetime import datetime


class Userr:
    def __init__(self, username, email) -> None:
        self.username = username
        # self._email = email
        self.__email = email

    def _get_email(self):  # Protected meethod
        print(f"Email accessed at {datetime.now()}")
        return self.__email

    def __set_email(self, new_email):  # Private method
        if "@" in new_email:
            self.__email = new_email


user1 = Userr("Soner", "kdsakfds@fdklskf.io")
print(user1._get_email())

user1.__set_email(("sonersg@outlook.com"))
