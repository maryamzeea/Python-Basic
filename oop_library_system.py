print("Welcome to OOP Library System!")

class Book:
    def __init__(self, title, author,available):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,title,author,available):
        new_book = Book(title,author,available)
        self.books.append(new_book)
        return f"'{title}' by {author} has been {available} to the library!"


    def display_books(self):
        if not self.books:
            print("No books available!")
        else:
            for book in self.books:
                status = "Available" if book.available else "Not Available"
                print(f"{book.title} by {book.author} is {status}")
            print()

    def book_borrow(self):
        for book in self.books:
            if book.title.lower()==book.title:
                if book.available:
                    print(f"{book.title} borrowed!")
                else:
                    print(f"{book.title} was not available!")

    def return_book(self):
        for book in self.books:
            if book.available:
                print(f"{book.title} returned!")
            else:
                print(f"{book.title} was not borrowed!")

library = Library()

while True:
    print("Menu")
    print("1. Add a book")
    print("2. Display a book")
    print("3. Return a book")
    print("4. Borrow a book")
    print("5. Exit the library")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_name = input("Enter book name: ")
        author = input("Enter book author: ")
        library.add_book(author,book_name,True)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book_name = input("Enter book name: ")
        author = input("Enter book author: ")
        library.return_book()

    elif choice == "4":
        book_name = input("Enter book name: ")
        author = input("Enter book author: ")
        library.book_borrow()

    else:
        print("You may exit the library.")
    break




