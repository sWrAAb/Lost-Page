import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'TheLostPage'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/books')
def books():
    return render_template("books.html", books=mongo.db.books.find())

@app.route('/categories')
def categories():
    return render_template("categories.html", books=mongo.db.categories.find())

@app.route('/add_book')
def add_book():
    return render_template("addbook.html")

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)