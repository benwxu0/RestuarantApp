class MealItem:
    def __init__(self, ID:int, quantity: int):
        self.ID = ID
        self.quantity = quantity

    def updateQuantity(self, quantity: int):
        self.quantity = quantity