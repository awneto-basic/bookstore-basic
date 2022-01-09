from . import db
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
    format = db.Column(db.String(30), nullable=False)
    imageURL = db.Column(db.String(500))
    dateCreated = db.Column(db.DateTime(timezone=True), default=func.now())
    dateUpdated = db.Column(db.DateTime(timezone=True), default=func.now())

class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagName =  db.Column(db.String(30))

class BookTag(db.Model):
    __tablename__ = "booktag"
    book_ID = db.Column(db.Integer, db.ForeignKey("book.id"), primary_key=True, nullable=False)
    tag_ID = db.Column(db.Integer, db.ForeignKey("tag.id"), primary_key=True, nullable=False)

# TODO: I could also add a table of authors to enable search by author ID