from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library instance
    library = Library()

    # Create some books
    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    ebook = EBook("Snow Crash", "Neal Stephenson", 1992, 500)
    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)

    # Add books to the library
    library.add_book(classic_book)
    library.add_book(ebook)
    library.add_book(print_book)

    # List all books in the library
    library.list_books()

if __name__ == "__main__":
    main()
