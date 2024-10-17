class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.level = "User"

    def get_id(self):
        print(f"id - {self.id}")

    def get_name(self):
        print(f"name - {self.name}")

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.level = "Admin"
        self.__users = []

    def get_access_level(self):
        print(f"level - {self.level}")

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user):
        self.__users.remove(user)

    def list_users(self):
        for user in self.__users:
            print(user.get_name())

admin = Admin(1, "Admin")
user1 = User(2, "User1")
user2 = User(3, "User2")

admin.add_user(user1)
admin.add_user(user2)

admin.list_users()

admin.remove_user(user1)

admin.list_users()
