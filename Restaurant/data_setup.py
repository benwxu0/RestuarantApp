from __init__ import db, Role, Account, Menu, Item

db.drop_all()
db.create_all()

def initRole():
    role0 = Role(name='Customer')
    role1 = Role(name='Waiter')
    role2 = Role(name='Chef')
    role3 = Role(name='Manager')
    db.session.add_all([role0, role1, role2, role3])
    db.session.commit()

def insertData():
    a1 = Account(name='jing', email='jing@163.com', password='123456', role_id=4)
    db.session.add(a1)
    db.session.commit()

    menu1 = Menu(name='Spring Menu', description='New Food for New Season', user_id=a1.id)
    db.session.add(menu1)
    db.session.commit()
    #
    # menusection1 = MenuSection(name='Appetizer', description='Appetizer', menu_id=menu1.id)
    # menusection2 = MenuSection(name='Entree', description='Entree', menu_id=menu1.id)
    # menusection3 = MenuSection(name='Soup', description='Soup', menu_id=menu1.id)
    # db.session.add_all([menusection1, menusection2, menusection3])
    # db.session.commit()

    item1 = Item(name='Cheese Stick', description='Cheese', price='15', course='Appetizer', menu_id=menu1.id)
    item2 = Item(name='Steak', description='Beef', price='15', course='Entree', menu_id=menu1.id)
    item3 = Item(name='Ice Cream', description='Ice Cream', price='17', course='Dessert', menu_id=menu1.id)
    item4 = Item(name='Pumpkin Soup', description='Soup', price='9', course='Soup', menu_id=menu1.id)
    item5 = Item(name='Sparkling Water', description='Beverage', price='5', course='Beverage', menu_id=menu1.id)
    db.session.add_all([item1, item2, item3, item4, item5])
    db.session.commit()


def deleteData():
    role = Role.query.get(2)
    db.session.delete(role)
    db.session.commit()


def updateData():
    role = Role.query.get(2)
    role.name = 'Receptionist'
    db.session.commit()


def selectData():
    roles = Role.query.all()
    print(roles)
    for s in roles:
        print(s.name)

initRole()
insertData()

# selectData()

