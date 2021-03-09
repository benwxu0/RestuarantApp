from Restaurant.EnumTypes import OrderStatus
class Order:

    def __init__(self, ID: int, tableNum: str, status: OrderStatus):
        self.ID = ID
        self.tableNum = tableNum
        self.status = status

    def addMeal(self):
        pass

    def removeMeal(self):
        pass

    def setStatus(self) -> OrderStatus:
        pass