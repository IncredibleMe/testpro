#auti einai mia klasi gia to Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def to_string(self):
        return f"{self.title},{self.author}"
    
    @staticmethod
    def from_string(book_str):
        title, author = book_str.strip().split(',')
        return Book(title, author)
