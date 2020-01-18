import os
import datetime
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
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
    adventure = mongo.db.books.find( { 'genre':' Adventure'} )
    comedy = mongo.db.books.find( { 'genre':' Comedy'} )
    divination = mongo.db.books.find( { 'genre':'Divination'} )
    fantasy = mongo.db.books.find( { 'genre':'Fantasy'} )
    fiction = mongo.db.books.find( { 'genre':'Fiction'} )
    mystery = mongo.db.books.find( { 'genre':'Mystery'} )
    nonfiction = mongo.db.books.find( { 'genre':'Nonfiction'} )
    romance = mongo.db.books.find( { 'genre':'Romance'} )
    
    return render_template('books.html', 
                            books=mongo.db.books.find(), 
                            categories=mongo.db.categories.find(), 
                            adventure=adventure, 
                            comedy=comedy,
                            divination=divination,
                            fantasy=fantasy,
                            fiction=fiction,
                            mystery=mystery,
                            nonfiction=nonfiction,
                            romance=romance)
                                                        

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
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_books = mongo.db.books.find({"_id": ObjectId(book_id)})
    return render_template("viewbook.html", books = all_books, book=the_book)

# Edit book #

@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editbook.html', book=the_book, categories=all_categories)

# Update form #

@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.books
    books.update( {'_id': ObjectId(book_id)},
    {
        'title': request.form.get('title'),
        'author': request.form.get('author'),
        'year': request.form.get('year'),
        'genre': request.form.get('genre'),
        'cover_img': request.form.get('cover_img'),
        'description': request.form.get('description')
    })
    return redirect(url_for('books'))

# Delete book #

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('books'))

@app.context_processor
def books_total():
    books_count = mongo.db.books.count
    return dict(books_count=books_count)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)