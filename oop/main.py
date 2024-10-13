# main.py
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create an instance of Library
    library = Library()

    # Create different types of books
    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    ebook = EBook("Snow Crash", "Neal Stephenson", 1992, "KB", 500)
    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)

    # Add books to the library
    library.add_book(classic_book)
    library.add_book(ebook)
    library.add_book(print_book)

    # List all books in the library
    print("Books currently in the library:")
    for book in library.list_books():
        print(book)

    # Remove a book and list again
    library.remove_book(ebook)
    print("\nAfter removing the eBook:")
    for book in library.list_books():
        print(book)

if __name__ == "__main__":
    main()
