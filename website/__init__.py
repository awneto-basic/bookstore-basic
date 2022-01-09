from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "book_database.db"


def create_app():
    app = Flask(__name__)   # name of the file that was ran
    secret_key = "this is a test secret key avocado 341F1AS"  # encrypted cookies #TODO: remove reference for the secret key from the source code
    app.config["SECRET_KEY"] = secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    db.init_app(app)

    from .views import views
    from .api import api

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(api, url_prefix="/")
    from .models import Book

    create_database(app)


    return(app)


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Bookstore database created")

