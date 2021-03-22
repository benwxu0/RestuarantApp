class Bill:
    def __init__(self, ID: int, ammount: float, tip: float, tax: float, isPaid: bool):
        self.ID = ID
        self.amount = ammount
        self.tip = tip
        self.tax = tax
        self.isPaid = isPaid

    def createBill(self):
        return Bill(1,0,0,False)
