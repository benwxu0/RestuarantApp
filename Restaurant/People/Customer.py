from .Account import Account
from Restaurant.EnumTypes import UserType

class Customer(Account):
    def __init__(self, ID: int, password: str, name: str, email: str, phone: int):
        super().__init__(ID, password, name, email, phone, UserType.Customer)

    def createOrder(self):
        pass

