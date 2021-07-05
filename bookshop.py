from enum import unique
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import re
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'gdfgvbisbiubvcuyavcgyxyvEEFCUMNIFHbsbsdcvijb'

#Finding the current app path
project_dir = os.path.dirname(os.path.abspath(__file__))

#Creating a database file called "bookdatabase.db" in the path found above
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

#Connecting the database to the sqlalchemy dependency
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

#Conecting the app to the db
db = SQLAlchemy(app)

@app.before_first_request
def create_table():
    db.create_all()

#Creating a model for the book table
class Book(db.Model):
    email = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
def __repr__(self):
    return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
    #Validating the content of the form. 
    if request.form:
        #print(request.form)
        #print(project_dir)
        #book = Book(title = request.form.get('title'))
        title_from_form = request.form.get('title')
        email_from_form = request.form.get('email')
        
        book = Book(title=title_from_form, email=email_from_form)
    
        
        db.session.add(book) #adds data to session
        db.session.commit() #
        
    books = Book.query.all()
    return render_template('home.html', books = books)

#@app.route("/bookstore", )
#def temp():
#    return render_template('home.html')