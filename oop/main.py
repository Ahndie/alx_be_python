def main():
    # Adding the 'year' argument to the Book instantiation
    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    
    # EBook example with file size and format
    ebook = EBook("Snow Crash", "Neal Stephenson", 1992, "KB", 500)
    
    # PrintBook example with page count
    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)
    
    # Print the details of each book
    print(classic_book)
    print(ebook)
    print(print_book)

if __name__ == "__main__":
    main()
