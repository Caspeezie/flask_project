from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask import request

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

@app.before_first_request
def create_table():
    db.create_all()

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
def __repr__(self):
    return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        #print(request.form)
        #print(project_dir)
        #book = Book(title = request.form.get('title'))
        title_from_form = request.form.get('title')
        book = Book(title=title_from_form)
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template('home.html', books = books)

#@app.route("/bookstore", )
#def temp():
#    return render_template('home.html')