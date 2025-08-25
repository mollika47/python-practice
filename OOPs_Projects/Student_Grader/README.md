# Library Management System
 
Main Entities:
•	Book: title, author, ID, availability
•	User: name, ID, borrowed_books
•	LibrarySystem: manages books and users
Key Functions:
•	add_book(title, author, id)
	➤ Adds a new book to the library
•	remove_book(id)
	➤ Deletes a book from the system
•	borrow_book(user_id, book_id)
	➤ Lends a book to a user
•	return_book(user_id, book_id)
	➤ Returns a book from a user
•	view_available_books()
	➤ Shows all unborrowed books
•	view_user_books(user_id)
	➤ Lists books borrowed by a user
Expected Output:
•	Messages like “Book borrowed successfully”, lists of available books, user history, etc.
