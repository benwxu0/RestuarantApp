from Restaurant.Payment.Order import Order
from Restaurant.People.Account import Account
from Restaurant.EnumTypes import UserType

class Chef(Account):
    def __init__(self, ID: int, password: str, name: str, email: str, phone: int):
        super().__init__(ID, password, name, email, phone, UserType.Chef)

    def takeOrder(self):
        myOrder = Order()
        print("Cook Order :")
        print(myOrder)


