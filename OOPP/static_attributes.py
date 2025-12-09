############################################
# Static attributes:
############################################


class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1


user1 = User("Soner", "fkdsfkas@smail.com")
user2 = User("şinasi", "şinasi@smail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)
