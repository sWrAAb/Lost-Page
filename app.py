import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    return render_template('index.html', books=mongo.db.books.find())

@app.route('/books')
def books():
    return render_template('books.html', books=mongo.db.books.find())

@app.route('/categories')
def categories():
    
    return render_template('categories.html', books = mongo.db.books.find())

# Add a book to database #

@app.route('/add_book')
def add_book():
    return render_template('addbook.html',categories=mongo.db.categories.find(), book=mongo.db.books.find())

@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('books'))

# View book info #

@app.route('/view_book/<book_id>', methods=["GET", "POST"])    
def view_book(book_id):
    all_books = mongo.db.books.find({"_id": ObjectId(book_id)})
    return render_template("viewbook.html", books = all_books)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)