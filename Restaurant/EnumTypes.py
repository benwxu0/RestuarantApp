from enum import Enum

class OrderStatus(Enum):
    NONE = 0
    RECEIVED = 1
    PREPARING = 2
    COMPLETED = 3
    CANCELED = 4

class UserType(Enum):
    OTHER = 0
    Waiter = 1
    Customer = 2
    Cashier = 3
    Manager = 4
    Chef = 5
    Receptionist = 6
