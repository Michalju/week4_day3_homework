from flask import Flask, render_template, Blueprint, redirect, request
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("tasks", __name__)
# INDEX
# GET '/books'
@books_blueprint.route("/books")
def get_books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

# NEW
# GET '/books/new'


# CREATE
# POST '/books'


# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'

