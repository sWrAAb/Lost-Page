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

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)