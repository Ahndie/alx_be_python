# main.py

from library_management import Book, Library

def main():
    # Create a library
    library = Library()
    
    # Add books to the library
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # List available books
    print("Initial list of available books:")
    library.list_available_books()

    # Check out a book
    library.check_out_book("1984")
    print("\nList of available books after checking out '1984':")
    library.list_available_books()

    # Return the book
    library.return_book("1984")
    print("\nList of available books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
