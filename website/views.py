from flask import Blueprint, render_template, jsonify
from flask import request
from flask import flash
from .models import Book
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/", methods=["GET","POST"])  # homepage
def home():
    # TODO: Create method to add tags to books
    if request.method == "POST":
        print(request.form)
        title = request.form.get("bookTitle")
        author = request.form.get("author")
        edition = request.form.get("edition")
        description = request.form.get("description")
        price = request.form.get("price")
        currency = request.form.get("currency")
        quantity = request.form.get("quantity")
        book_format = request.form.get("format")
        image_URL = request.form.get("imageURL")

        book = Book.query.filter(Book.title == title, Book.edition == edition, Book.author == author).first() # check if an entry for this book already exists in the database

        if len(title) < 1:
            flash("Please add a name for the book", category="error")
        elif len(title) > 256:
            flash("Book title is too long.", category="error")
        elif len(author) < 1:
            flash("Please insert an author name", category="error")
        elif len(author) > 100:
            flash("Author name is too long", category="error")
        elif len(description) > 500:
            flash("Description is too long", category="error")
        elif len(price) < 1:
            flash("Please add the price for the book", category="error")
        elif float(price) < 0:
            flash("Invalid price.", category="error")
        elif len(currency) < 1:
            flash("Please add a currency for the price.", category="error")
        elif int(quantity) < 1:
            flash("Please add at least one book", category="error")
        elif book: # if there's a book with the same title
            book.quantity += int(quantity)   # add new books to an existing book entry
            db.session.commit()
        else:
            new_book = Book(
                title=title,
                author = author,
                edition = edition,
                description = description,
                price= round(float(price), 2),
                currency = currency,
                quantity = int(quantity),
                format = book_format,
                imageURL = image_URL
            )
            flash("Book added!", category="success")
            db.session.add(new_book)
            db.session.commit()
    books = Book.query.all()
    return (render_template("home.html", books=books))

@views.route("/delete-book", methods=["POST"])
def delete_book():
    book = json.loads(request.data)
    bookId = book["bookId"]
    book = Book.query.get(bookId)
    if book:
        db.session.delete(book)
        db.session.commit()
        print("Book deleted")
    return jsonify({})

@views.route("/books/<id>")
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

