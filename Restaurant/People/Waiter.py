from Restaurant.People.Account import Account
from Restaurant.EnumTypes import UserType

class Waiter(Account):
    def __init__(self, ID: int, password: str, name: str, email: str, phone: int):
        super().__init__(ID, password, name, email, phone, UserType.Waiter)

    def editOrder(self):
        pass

    def cancelOrder(self):
        pass