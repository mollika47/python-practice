class Book:
    def __init__(self, title, author, book_id,):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.status = "Available"

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Book ID: {self.book_id}, Status: {self.status}")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.user_borrowed = []
        self.count_books = 0

    def show_info(self):
        print(f"Name: {self.name}, ID: {self.user_id}, Book-borrowed: {self.count_books}")
        print([book.title for book in self.user_borrowed])

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
            self.books.append(book)
            print(f"'{book.title}' added to library")

    def add_user(self, user):
        self.users.append(user)
        print(f"New user:'{user.name}' added to library")

    def remove_book(self, book):
        self.books.remove(book)
        print(f"'{book.title}' removed from library")

    def borrow_book(self, book_id, user_id):
        book_found = None
        user_found = None

        for book in self.books:
            if book.book_id == book_id:
                book_found = book
                break

        if not book_found:
            print("Book not found")

        for user in self.users:
            if user.user_id == user_id:
                user_found = user
                break

        if not user_found:
            print("User not found")

        if book_found and user_found:
            if book_found.status == "Available":
                book.status = "Borrowed"
                user_found.count_books += 1
                user.user_borrowed.append(book_found)
                print(f"'{book.title}' borrowed by '{user.name}' ID: {user.user_id}")
            else:
                print(f"{book.title} already borrowed")

    def return_book(self, book_id, user_id):
        found_book = None
        found_user = None

        for book in self.books:
            if book.book_id == book_id and book.status == "Borrowed":
                found_book = book
                break

        if not found_book:
            print("Book doesn't match.")

        for user in self.users:
            if user.user_id == user_id and user.count_books > 0:
                found_user = user
                break

        if not found_user:
            print("User doesn't match.")

        if found_book and found_user:
            book.status = "Available"
            user.user_borrowed.remove(found_book)
            found_user.count_books -= 1
            print(f"'{book.title}' has returned")

    def show_borrowed_by(self):
        borrowed_by = {}
        for user in self.users:
            if user.user_borrowed:
                key = user.user_id
                borrowed_by[key] = [book.title for book in user.user_borrowed]
        print(borrowed_by)

    def show_available_books(self):
        print("Showing available books:")
        found = False
        for book in self.books:
            if book.status == "Available":
                print(f"{book.title} by {book.author} - available")
                found = True
        if not found:
            print("None")

    def show_books(self):
        print(f"Book List: ")
        for book in self.books:
            book.show_info()

    def show_users(self):
        print(f"User List: ")
        for user in self.users:
            user.show_info()




book1 = Book("The Witcher", "J.H Strode", 453701)
book2 = Book("The Screaming Staircase", "J.H Strode", 453702)
book3 = Book("Harmony", "Whitney Hanson", 453703)
book4 = Book("Tragedy", "L.T. Luis", 453704)
book5 = Book("That Summer", "Johnathan", 453705)
book6 = Book("In The Woods", "Nick Willer", 453706)

u101 = User("Millie", 101)
u102 = User("Barb", 102)
u103 = User("Kate", 103)

library = LibrarySystem()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)

library.add_user(u101)
library.add_user(u102)
library.add_user(u103)

library.remove_book(book4)

library.borrow_book(453701, 101)
library.borrow_book(453703, 101)
library.borrow_book(453702, 102)

library.show_users()
library.show_books()
library.show_available_books()