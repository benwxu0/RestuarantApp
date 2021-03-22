from Restaurant.Menu.Meal import Meal
rom flask import Flask
from flask import render_template, request, redirect, jsonify, url_for, flash
from flask_sqlalchemy import SQLAlchemy

class MealItem:
    def __init__(self, ID:int, quantity: int):
        self.ID = db.Column(db.Integer, primary_key=True)
        self.quantity = 0

    def updateQuantity(self, quantity: int):
        updateQuantity = Meal()
        self.quantity = quantity + updateQuantity.counter
        