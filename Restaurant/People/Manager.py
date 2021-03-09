from Restaurant.People.Account import Account
from Restaurant.EnumTypes import UserType

class Manager(Account):
    def __init__(self, ID: int, password: str, name: str, email: str, phone: int):
        super().__init__(ID, password, name, email, phone, UserType.Manager)

    def createMenu(self):
        pass

    def editMenu(self):
        pass