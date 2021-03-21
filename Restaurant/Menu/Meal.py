from Restaurant.Menu.MealItem import MealItem
class Meal:
    def __init__(self, ID: int, counter: int):
        self.ID = 1
        self.counter = 0


    def addMealItem(self):
        addMeal=MealItem()
        ID= addMeal.ID
        counter = 1

    def removeMealItem(self):
        removeMeal = MealItem()
        print('Remove an item? (Y or N)')
        x=input()
        if x == 'Y':
            removeID = input()
            if removeID == removeMeal.ID:
                removeMeal=None
                MealItem(removeMeal)
                counter = -1



                
