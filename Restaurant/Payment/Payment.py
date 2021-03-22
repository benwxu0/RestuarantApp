from datetime import datetime
from Restaurant.Payment.Bill import Bill

class Payment:
    def __init__(self, id: int, amount: float, createDate: datetime, creditCardName: str, cardNum: int, expireDate: datetime):
        self.id = id;
        self.amount = amount;
        self.createDate = createDate
        self.creditCardName = creditCardName
        self.cardNum = cardNum

    def pay(self, bill: Bill):
        bill.isPaid = True
        return bill