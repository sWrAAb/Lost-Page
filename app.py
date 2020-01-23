import os
from flask import Flask, redirect, render_template, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
import re

# create instance of flask and assign it to app


app = Flask(__name__)


# MongoDB URI / Assign database


app.config["MONGO_DBNAME"] = 'TheLostPage'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', books=mongo.db.books.find())


# ----- READ ALL ----- #


@app.route('/books')
def books():
    """
    Read all books from database.
    Display all books initially, with option to Search.
    Search function works by reading args for existing data.
    """
    return render_template('books.html',
                            books=mongo.db.books.find(),
                            categories=mongo.db.categories.find())

# Search books


@app.route('/search')
def search():
    '''
    Search books by keywords. Any letter however had to leave it
    case sensitive. If i add /i bug apears
    '''
    user_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(user_query))}
    result = mongo.db.books.find({
        '$or': [
            {'title': query},
            {'author': query},
            {'genre': query},
        ]
    })
    return render_template('search_results.html',
                            query=user_query,
                            books=result)


@app.route('/categories')
def categories():

    return render_template('categories.html', books=mongo.db.books.find())


#    CRUD: Create | Read | Update | Delete    #


# --CREATE-- #

@app.route('/add_book')
def add_book():
    return render_template('addbook.html',
                            categories=mongo.db.categories.find(),
                            book=mongo.db.books.find())


@app.route('/insert_book', methods=['POST'])
def insert_book():
    """
    Create book in database.
    Inject all form data to new book document on submit.
    """
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('books'))


# ----- READ ONE ----- #


@app.route('/view_book/<book_id>', methods=["GET", "POST"])
def view_book(book_id):
    """
    Read book in database.
    Gather details from document for displaying to user.
    """
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_books = mongo.db.books.find({"_id": ObjectId(book_id)})
    return render_template("viewbook.html", books=all_books, book=the_book)


# ----- UPDATE ----- #


@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    """
    Update book in database.
    Inject all existing data from the book back into the form.
    Bug alert. Description text area returns empty.
    """
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editbook.html',
                            book=the_book,
                            categories=all_categories)


# ----- UPDATE FORM ----- #


@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.books
    books.update({'_id': ObjectId(book_id)},
    {
        'title': request.form.get('title'),
        'author': request.form.get('author'),
        'year': request.form.get('year'),
        'genre': request.form.get('genre'),
        'cover_img': request.form.get('cover_img'),
        'description': request.form.get('description')
    })
    return redirect(url_for('books'))


# ----- DELETE ----- #


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    """
    Removes book from database.
    """
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('books'))


@app.context_processor
def books_total():
    """
    Show total number of books in collection.
    Displayed in navbar.
    """
    books_count = mongo.db.books.count
    return dict(books_count=books_count)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
