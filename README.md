# bookstore-basic
A basic bookstore showcase page built with Flask.

### Features
- Adding and removing books using forms and buttons on the page
- Viewing information for books in stock
- Accessing bookstore database via API 

### Accessing the platform
To access the bookstore, go to https://api-bookstore-2022-01.herokuapp.com/

### API
Server exposes books via API. The following operations are supported:
- Get book information given the book ID number
- Create a book given book information
- Update book information given its ID
- List books by author

##### API: Get book by ID
Example:
- Run https://api-bookstore-2022-01.herokuapp.com/api/books/3
- Information for the book with id = 3 will be exposed.
> {
	"author":"Jon Bodner",
	"currency":"GBP",
	"description":"Go is rapidly becoming the preferred language for building web services. While there are plenty of tutorials available that teach Go's syntax to developers with experience in other programming languages, tutorials aren't enough. They don't teach Go's idioms, so developers end up recreating patterns that don't make sense in a Go context. This practical guide provides the essential background you need to write clear and idiomatic Go.",
	"edition":"1",
	"format":"Hard copy",
	"imageURL":"https://images-na.ssl-images-amazon.com/images/I/41zmzWx2CpL._SX379_BO1,204,203,200_.jpg","price":"35.00","quantity":1,
	"title":"Learning Go: An Idiomatic Approach to Real-World Go Programming"
	}

##### API: Create book given book information
Example:
- Use the following request (written in *json*) to add 10 copies of a book to the server:
> {
	"author":"Jon Bodner",
	"currency":"GBP",
	"description":"Go is rapidly becoming the preferred language for building web services. While there are plenty of tutorials available that teach Go's syntax to developers with experience in other programming languages, tutorials aren't enough. They don't teach Go's idioms, so developers end up recreating patterns that don't make sense in a Go context. This practical guide provides the essential background you need to write clear and idiomatic Go.",
	"edition":"1",
	"format":"Hard copy",
	"imageURL":"https://images-na.ssl-images-amazon.com/images/I/41zmzWx2CpL._SX379_BO1,204,203,200_.jpg","price":"35.00",
	"quantity":10,
	"title":"Learning Go: An Idiomatic Approach to Real-World Go Programming"
	}



- Using Postman, send a POST request to  https://api-bookstore-2022-01.herokuapp.com/api/books
- 





### Not implemented on this build:
- Tags (e.g. Fiction, non-fiction)
- Purchasing operations
