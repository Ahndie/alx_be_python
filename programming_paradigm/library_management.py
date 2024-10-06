# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title: str, author: str):
        self.title = title          # Public attribute for the book's title
        self.author = author        # Public attribute for the book's author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_checked_out(self):
        """Return whether the book is checked out or not."""
        return self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author}"


class Library:
    """A class representing a collection of books in a library."""
    
    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book: Book):
        """Add a book to the library."""
        self._books.append(book)

    def list_available_books(self):
        """List all books that are available (not checked out)."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books are available.")

    def check_out_book(self, title: str):
        """Check out a book by its title if it is available."""
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f"Book '{title}' has been checked out.")
                return
        print(f"Book '{title}' is not available or already checked out.")

    def return_book(self, title: str):
        """Return a book to the library by its title."""
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' was not checked out.")
