class Book: 
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication year

    def __str__(self):
    	return f"{self.title} by {self.author}, published in {self.publication_year}"

    def __repr__(self):
    	return f"Book(title={self.title}, author={self.author}, publication_year={self.publication_year})"
    	
    	