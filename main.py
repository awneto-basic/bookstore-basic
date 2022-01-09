from website import create_app

app_bookstore = create_app()

if __name__ == "__main__":
    app_bookstore.run(debug=False)

