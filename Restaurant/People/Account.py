from Restaurant.EnumTypes import UserType

class Account:
    def __init__(self, ID: int, password: str, name: str, email: str, phone: int, userType: UserType):
        self.ID = ID
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.userType = userType

    def __str__(self):
        return f"ID: {self.ID}\nName: {self.name}\nemail:{self.email}"

    def resetPassword(self, password):
        self.password = password


if __name__ == '__main__':
    testAcc = Account(1,'asdff','ben','@gmail.com',1111,UserType.Chef)
    print(testAcc)
    print("hello world")

