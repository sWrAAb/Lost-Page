import os
from flask import Flask, render_template
from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'TheLostPage'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


@app.route('/')
@app.route('/books')
def books():
    return render_template("books.html")

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)