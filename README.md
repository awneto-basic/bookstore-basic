# bookstore-basic 📚
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
- Information for the book with id = 3, formatted in _json_, will be exposed.
> {
	"author":"Jon Bodner",
	"currency":"GBP",
	"description":"Go is rapidly becoming the preferred language for building web services. While there are plenty of tutorials available that teach Go's syntax to developers with experience in other programming languages, tutorials aren't enough. They don't teach Go's idioms, so developers end up recreating patterns that don't make sense in a Go context. This practical guide provides the essential background you need to write clear and idiomatic Go.",
	"edition":"1",
	"format":"Hard copy",
	"imageURL":"https://images-na.ssl-images-amazon.com/images/I/41zmzWx2CpL._SX379_BO1,204,203,200_.jpg",
	"price":"35.00",
	"quantity":1,
	"title":"Learning Go: An Idiomatic Approach to Real-World Go Programming"
	}
	
##### API: Get books given an author
Example:
- Run https://api-bookstore-2022-01.herokuapp.com/api/books/authors/Plato
- Information for the books written by Plato, formatted in _json_, will be exposed.
>{
	"books":
		[
			{
				"author":"Plato",
				"currency":"GBP",
				"description":"The second edition of Five Dialogues presents G. M. A. Grube's distinguished translations, as revised by John Cooper for Plato, Complete Works. A number of new or expanded footnotes are also included along with an updated bibliography.",
				"edition":"123",
				"format":"Hard copy",
				"imageURL":"https://images-na.ssl-images-amazon.com/images/I/417Z4CIfomL._SX314_BO1,204,203,200_.jpg",
				"price":"30.00",
				"quantity":1,
				"title":"Plato: Five Dialogues: Euthyphro, Apology, Crito, Meno, Phaedo"
			},
			{
				"author":"Plato",
				"currency":"GBP",
				"description":"Presented in the form of a dialogue between Socrates and three different interlocutors, it is an inquiry into the notion of a perfect community and the ideal individual within it. During the conversation other questions are raised: what is goodness; what is reality; what is knowledge; what is the purpose of education? With remarkable lucidity and deft use of allegory, Plato arrives at a depiction of a state bound by harmony and ruled by 'philosopher kings'.",
				"edition":"141",
				"format":"Hard copy",
				"imageURL":"https://images-na.ssl-images-amazon.com/images/I/413HlIU9zhL._SX324_BO1,204,203,200_.jpg",
				"price":"3.99",
				"quantity":5,
				"title":"The Republic"
			},
			{
				"author":"Plato",
				"currency":"GBP",
				"description":"In the course of a lively drinking party, a group of Athenian intellectuals exchange views on eros, or desire. From their conversation emerges a series of subtle reflections on gender roles, sex in society and the sublimation of basic human instincts.",
				"edition":"190",
				"format":"eBook",
				"imageURL":"https://images-na.ssl-images-amazon.com/images/I/41r9XQblMqL._SX322_BO1,204,203,200_.jpg",
				"price":"0.99",
				"quantity":21,
				"title":"The Symposium"
			},
			{
				"author":"Plato",
				"currency":"GBP",
				"description":"The trial and condemnation of Socrates on charges of heresy and corrupting young minds is a defining moment in the history of classical Athens. ",
				"edition":"158",
				"format":"eBook",
				"imageURL":"https://images-na.ssl-images-amazon.com/images/I/518Vb776nNL._SX323_BO1,204,203,200_.jpg",
				"price":"0.99",
				"quantity":12,
				"title":"The Last Days of Socrates"
			}
		]
}
	

##### API: Add a book given book information
Example:
- Use the following request (written in *json*) to add 10 copies of a book to the server:
> {
	"author":"Jon Bodner",
	"currency":"GBP",
	"description":"Go is rapidly becoming the preferred language for building web services. While there are plenty of tutorials available that teach Go's syntax to developers with experience in other programming languages, tutorials aren't enough. They don't teach Go's idioms, so developers end up recreating patterns that don't make sense in a Go context. This practical guide provides the essential background you need to write clear and idiomatic Go.",
	"edition":"1",
	"format":"Hard copy",
	"imageURL":"https://images-na.ssl-images-amazon.com/images/I/41zmzWx2CpL._SX379_BO1,204,203,200_.jpg",
	"price":"35.00",
	"quantity":10,
	"title":"Learning Go: An Idiomatic Approach to Real-World Go Programming"
	}
	
- Using Postman, send a POST request using the _json_-formated data above to  https://api-bookstore-2022-01.herokuapp.com/api/books
- If the book already exists, the number of books in stock for this entry will be updated.
- If the book isn't in the database already, then an entry for the book will be added to the database.

##### API: Update book information given its ID
Example:
- Updating the book with ID = 3
- Use the following request (written in *json*) to update information of a book that is already included in the server:
> {
	"author":"Jon Bodner",
	"currency":"GBP",
	"description":"Go is rapidly becoming the preferred language for building web services. While there are plenty of tutorials available that teach Go's syntax to developers with experience in other programming languages, tutorials aren't enough. They don't teach Go's idioms, so developers end up recreating patterns that don't make sense in a Go context. This practical guide provides the essential background you need to write clear and idiomatic Go.",
	"edition":"1",
	"format":"Hard copy",
	"imageURL":"https://images-na.ssl-images-amazon.com/images/I/41zmzWx2CpL._SX379_BO1,204,203,200_.jpg",
	"price":"35.00",
	"quantity":2,
	"title":"Learning Go: An Idiomatic Approach to Real-World Go Programming"
	}
	
- Using Postman, send a PUT request using the _json_-formated data above to  https://api-bookstore-2022-01.herokuapp.com/api/books/3




### Not implemented on this build:
- Tags (e.g. Fiction, non-fiction)
- Purchasing operations
