from flask import Blueprint, jsonify
from flask import request
from flask import flash
from .models import Book
from . import db
from sqlalchemy.sql import func

import json

api = Blueprint("api", __name__)

#   GET
@api.route("/api/books/<id>")
def get_book(id):
    book = Book.query.get_or_404(id)
    #json formatting - RFC 8259
    return ({
                "title": book.title,
                "author": book.author,
                "edition": book.edition,
                "description": book.description,
                "price": book.price,
                "currency": book.currency,
                "quantity": book.quantity,
                "format": book.format,
                "imageURL": book.imageURL
             })

# CREATE / ADD
@api.route("/api/books", methods=["POST"])
def add_book():
    book = Book(
        title=request.json["title"],
        author=request.json["author"],
        edition = request.json["edition"],
        description = request.json["description"],
        price = request.json["price"],
        currency = request.json["currency"],
        quantity=request.json["quantity"],
        format=request.json["format"],
        imageURL=request.json["imageURL"])

    book_exists = Book.query.filter(
        Book.title == book.title,
        Book.edition == book.edition,
        Book.author == book.author).first() # check if an entry for this book already exists in the database

    if validate_book_entry(book):
        if book_exists:
            book_exists.quantity += int(book.quantity)   # add new books to an existing book entry
        else:
            db.session.add(book)

        db.session.commit()
        #json formatting - RFC 8259
        return ({
                    "title": book.title,
                    "author": book.author,
                    "edition": book.edition,
                    "description": book.description,
                    "price": book.price,
                    "currency": book.currency,
                    "quantity": book.quantity,
                    "format": book.format,
                    "imageURL": book.imageURL
                 })
    else:
        return("Invalid book data.")


# UPDATE (PUT)
@api.route("/api/books/<id>", methods=["PUT"])
def update_book(id):
    book = Book(
        title=request.json["title"],
        author=request.json["author"],
        edition = request.json["edition"],
        description = request.json["description"],
        price = request.json["price"],
        currency = request.json["currency"],
        quantity=request.json["quantity"],
        format=request.json["format"],
        imageURL=request.json["imageURL"],
        dateUpdated=func.now())

    book_exists = Book.query.filter_by(id=id).first()   # check if an entry for this book already exists in the database

    if validate_book_entry(book):
        if book_exists:

            book_exists.title = book.title
            book_exists.author = book.author
            book_exists.edition = book.edition
            book_exists.description = book.description
            book_exists.price = round(float(book.price), 2)
            book_exists.currency = book.currency
            book_exists.quantity = int(book.quantity)
            book_exists.format = book.format
            book_exists.imageURL = book.imageURL

            db.session.commit() # update book entry

            #json formatting - RFC 8259
            return ({
                        "title": book.title,
                        "author": book.author,
                        "edition": book.edition,
                        "description": book.description,
                        "price": book.price,
                        "currency": book.currency,
                        "quantity": book.quantity,
                        "format": book.format,
                        "imageURL": book.imageURL
                     })
        else:
            return("Book does not exist.")
    else:
        return("Invalid book data.")


# GET BY AUTHOR
@api.route("/api/books/authors/<author>")
def get_books_by_author(author):
    books = Book.query.filter_by(author=author)
    output = []
    for book in books:
        books_data = {
            "title": book.title,
            "author": book.author,
            "edition": book.edition,
            "description": book.description,
            "price": book.price,
            "currency": book.currency,
            "quantity": book.quantity,
            "format": book.format,
            "imageURL": book.imageURL
        }
        output.append(books_data)
    return{"books": output}

def validate_book_entry(book):
    b = True
    if len(book.title) < 1:
        b = False
    elif len(book.title) > 256:
        b = False
    elif len(book.author) < 1:
        b = False
    elif len(book.author) > 100:
        b = False
    elif len(book.description) > 500:
        b = False
    elif len(book.price) < 1:
        b = False
    elif float(book.price) < 0:
        b = False
    elif len(book.currency) < 1:
        b = False
    elif int(book.quantity) < 1:
        b = False

    return(b)