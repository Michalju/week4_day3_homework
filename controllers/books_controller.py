from flask import Flask, render_template, Blueprint, redirect, request
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def get_books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new")
def new_book():
    pass
    authors = author_repository.select_all()
    return render_template("books/new.html", authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    author = author_repository.select(request.form['author_id'])
  
    book = Book(request.form['title'], request.form['genre'], request.form['publisher'], author)
 
    book_repository.save(book)
    return redirect('/books') 

# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/show", methods=["POST"])
def show_book():
    book = book_repository.select(request.form['book_id'])
    return render_template("books/show.html", book = book)

# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/delete", methods=["POST"])
def delete_task():
    book_repository.delete(request.form['book_id'])
    return redirect('/books')
