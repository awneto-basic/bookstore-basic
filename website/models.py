from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func




class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), unique=True)
    author = db.Column(db.String(100), nullable=False)
    edition = db.Column(db.String(50))
    description = db.Column(db.String(500))
    price = db.Column(db.DECIMAL(10,2), nullable=False)
    currency = db.Column(db.String(4), nullable=False) # currency code: USD, GBP, BRL, EUR etc.
    quantity = db.Column(db.Integer)
    type = db.Column(db.String(30), nullable=False)
    imageURL = db.Column(db.String(500))
    tags = db.relationship("Tag")

class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bookID = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    tagName =  db.Column(db.String(30))

