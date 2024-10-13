# library_system.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, year={self.year})"


class EBook(Book):
    def __init__(self, title, author, year, file_format, file_size):
        super().__init__(title, author, year)
        self.file_format = file_format
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook in {self.file_format} format, {self.file_size} MB)"


class PrintBook(Book):
    def __init__(self, title, author, year, num_pages):
        super().__init__(title, author, year)
        self.num_pages = num_pages

    def __str__(self):
        return f"{super().__str__()} (PrintBook with {self.num_pages} pages)"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        return [str(book) for book in self.books]
