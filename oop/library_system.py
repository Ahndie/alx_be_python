# library_system.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"


class EBook(Book):
    def __init__(self, title, author, year, file_format, file_size):
        super().__init__(title, author, year)
        self.file_format = file_format
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}{self.file_format}"


class PrintBook(Book):
    def __init__(self, title, author, year, page_count):
        super().__init__(title, author, year)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list to hold books

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def remove_book(self, book):
        """Remove a book from the library."""
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        """List all books in the library."""
        return [str(book) for book in self.books]
