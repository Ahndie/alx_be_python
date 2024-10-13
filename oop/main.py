# main.py

def main():
    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    
    # EBook example
    ebook = EBook("Snow Crash", "Neal Stephenson", 1992, "KB", 500)
    
    # PrintBook example
    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)
    
    # Print the results
    print(classic_book)
    print(ebook)
    print(print_book)


if __name__ == "__main__":
    main()