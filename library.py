from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.filename = "books.txt"
    
    def add_book(self, book):
        self.books.append(book)
        self._save_books()
    
    def remove_book(self, title):
        for book in self.books[:]:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed successfully!")
                self._save_books()
                return
        print(f"Book '{title}' not found!")
    
    def list_books(self):
        if not self.books:
            print("No books in the library!")
            return
        
        print("\nBooks in library:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
    
    def search_books(self, search_term):
        found_books = []
        search_term = search_term.lower()
        
        for book in self.books:
            if (search_term in book.title.lower() or 
                search_term in book.author.lower()):
                found_books.append(book)
        
        if found_books:
            print("\nFound books:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. {book}")
        else:
            print("No matching books found!")
    
    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip():
                        self.books.append(Book.from_string(line))
        except FileNotFoundError:
            # Create the file if it doesn't exist
            open(self.filename, 'w').close()
    
    def _save_books(self):
        with open(self.filename, 'w') as file:
            for book in self.books:
                file.write(book.to_string() + '\n')

def main():
    # Initialize library
    library = Library()
    
    # Load existing books from file
    library.load_books()
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Add book")
        print("2. List all books")
        print("3. Search book")
        print("4. Remove book")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book = Book(title, author)
            library.add_book(book)
            print("Book added successfully!")
            
        elif choice == '2':
            library.list_books()
            
        elif choice == '3':
            search_term = input("Enter title or author to search: ")
            library.search_books(search_term)
            
        elif choice == '4':
            title = input("Enter book title to remove: ")
            library.remove_book(title)
            
        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
