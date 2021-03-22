from Restaurant.EnumTypes import OrderStatus
from Restaurant.Menu.Meal import Meal
class Order:

    def __init__(self, ID: int, tableNum: str, status: OrderStatus):
        self.ID = 1
        self.tableNum = tableNum
        self.status = status
        self.mealList = []

    def addMeal(self, meal: Meal):
        self.mealList.append(meal)

    def removeMeal(self, meal: Meal):
        self.mealList.remove(meal)

    def setStatus(self, status: OrderStatus) -> OrderStatus:
        self.status = status
