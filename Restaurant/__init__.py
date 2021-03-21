'''
Jingyi Huang
03/21/2021
'''

from flask import Flask
from flask import render_template, request, redirect, jsonify, url_for, flash
from flask_sqlalchemy import SQLAlchemy


# Creates the application object
app = Flask(__name__)

# Adding Secret Key to our App
app.secret_key = 'make this hard to guess!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Creating the User table to track the users creating/adding items to the tables:
# Role, Account, Menu, MenuSection and Item
class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    user = db.relationship('Account', backref='role')

    def __repr__(self):
        return '<Role: %s %s>' % (self.name, self.id)

class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False)
    mobile = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(250), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return '<User: %s %s %s>' % (self.name,  self.email, self.password)

# Creating the Menu tableS
class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    #menusections = db.relationship('MenuSection', cascade='delete, delete-orphan')
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    user = db.relationship(Account)


# Creating the MenuSection table
# class MenuSection(db.Model):
#     __tablename__ = 'menusection'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(250), nullable=False)
#     description = db.Column(db.String(250), nullable=False)
#     menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
#     #menuitems = db.relationship('Item', cascade='delete, delete-orphan')


# Creating the Item table
class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    # menusections_id = db.Column(db.Integer, db.ForeignKey('menusection.id'))

    # This method is for extracting the list of menu items in JSON format
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course,
        }


def getUserInfo(user_id):
    user = db.session.query(Account).filter_by(id=user_id).one()
    return user

# views from Menu module
@app.route('/')
@app.route('/index')
def index():
    menus = db.session.query(Menu).all()
    return render_template('restaurant.html', menus = menus)

# Show a restaurant menu
@app.route('/menu/<int:menu_id>/')
def showMenu(menu_id):
    menu = db.session.query(Menu).filter_by(id=menu_id).one()
    creator = getUserInfo(menu.user_id)
    items = db.session.query(Item).filter_by(menu_id=menu_id).all()

    return render_template('menu.html', items=items, menu=menu, creator=creator)


# Create a new menu item
@app.route('/menu/<int:menu_id>/new', methods=['GET', 'POST'])
def newMenuItem(menu_id):
    menu = db.session.query(Menu).filter_by(id=menu_id).one()
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form['description'], price=request.form[
                               'price'], course=request.form['course'], menu_id=menu_id)
        db.session.add(newItem)
        db.session.commit()
        flash('New Menu %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('showMenu', menu_id=menu_id))
    else:
        return render_template('newmenuitem.html', menu_id=menu_id)

# Edit a menu item
@app.route('/menu/<int:menu_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def editMenuItem(menu_id, item_id):
    editedItem = db.session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        db.session.add(editedItem)
        db.session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('showMenu', menu_id=menu_id))
    else:
        return render_template('editmenuitem.html', menu_id=menu_id, item=editedItem)

# Delete a menu item
@app.route('/menu/<int:menu_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(menu_id, item_id):
    itemToDelete = db.session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        db.session.delete(itemToDelete)
        db.session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showMenu', menu_id=menu_id))
    else:
        return render_template('deleteMenuItem.html', menu_id=menu_id, item=itemToDelete)


if __name__ == '__main__':
   app.run(debug = True)





