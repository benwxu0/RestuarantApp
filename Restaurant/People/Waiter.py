from Restaurant.People.Account import Account
from Restaurant.EnumTypes import UserType
from Restaurant.Payment.Order import Order

class Waiter(Account):
    def __init__(self, ID: int, password: str, name: str, email: str, phone: int):
        super().__init__(ID, password, name, email, phone, UserType.Waiter)

    def editOrder(self):
         changeOrder= Order()
         print('Change order? (Y/N)')
         change = input()
         if change == 'Y':
           
            newID = input()
            newTble = input()
            newStatus = input()
            Order.ID = newID
            Order.tableNum= newTble
            Order.status=newStatus

        


    def cancelOrder(self):
         cancelOrder= Order()
         print('Cancel order? (Y/N)')
         cancel = input()
         if cancel == 'Y':
             cancelOrder=None
             Order(cancelOrder)
