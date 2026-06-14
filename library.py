"""
Library Management System class.
Integrates Book and Member classes to manage library operations.
"""

from book import Book
from member import Member, Student, Faculty, Researcher


class Library:
    """Main library management system."""
    
    def __init__(self, name):
        """
        Initialize the Library system.
        
        Args:
            name (str): Name of the library
        """
        self.name = name
        self.__books = {}  # Dictionary to store books (ISBN -> Book)
        self.__members = {}  # Dictionary to store members (member_id -> Member)
    
    def add_book(self, title, author, isbn):
        """
        Add a new book to the library.
        
        Args:
            title (str): Book title
            author (str): Book author
            isbn (str): Book ISBN
            
        Returns:
            Book: The created Book object
        """
        if isbn in self.__books:
            print(f"Book with ISBN {isbn} already exists")
            return self.__books[isbn]
        
        book = Book(title, author, isbn)
        self.__books[isbn] = book
        print(f"Added book: {title}")
        return book
    
    def add_member(self, member):
        """
        Add a new member to the library.
        
        Args:
            member (Member): Member object to add
            
        Returns:
            bool: True if added successfully, False otherwise
        """
        if member.member_id in self.__members:
            print(f"Member with ID {member.member_id} already exists")
            return False
        
        self.__members[member.member_id] = member
        print(f"Added member: {member.name}")
        return True
    
    def get_book(self, isbn):
        """
        Get a book by ISBN.
        
        Args:
            isbn (str): Book ISBN
            
        Returns:
            Book: Book object if found, None otherwise
        """
        return self.__books.get(isbn)
    
    def get_member(self, member_id):
        """
        Get a member by ID.
        
        Args:
            member_id (str): Member ID
            
        Returns:
            Member: Member object if found, None otherwise
        """
        return self.__members.get(member_id)
    
    def list_all_books(self):
        """List all books in the library."""
        print(f"\n=== All Books in {self.name} ===")
        if not self.__books:
            print("No books available")
            return
        
        for isbn, book in self.__books.items():
            print(f"[{isbn}] {book}")
    
    def list_available_books(self):
        """List all available books."""
        print(f"\n=== Available Books in {self.name} ===")
        available = [book for book in self.__books.values() if book.is_available()]
        
        if not available:
            print("No books available")
            return
        
        for book in available:
            print(f"[{book.isbn}] {book}")
    
    def list_all_members(self):
        """List all members of the library."""
        print(f"\n=== All Members of {self.name} ===")
        if not self.__members:
            print("No members registered")
            return
        
        for member_id, member in self.__members.items():
            member.display_info()
    
    def process_borrow(self, member_id, isbn):
        """
        Process a book borrow request.
        
        Args:
            member_id (str): Member ID
            isbn (str): Book ISBN
            
        Returns:
            bool: True if successful, False otherwise
        """
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        
        if not member:
            print(f"Member with ID {member_id} not found")
            return False
        
        if not book:
            print(f"Book with ISBN {isbn} not found")
            return False
        
        return member.borrow_book(book)
    
    def process_return(self, member_id, isbn):
        """
        Process a book return request.
        
        Args:
            member_id (str): Member ID
            isbn (str): Book ISBN
            
        Returns:
            bool: True if successful, False otherwise
        """
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        
        if not member:
            print(f"Member with ID {member_id} not found")
            return False
        
        if not book:
            print(f"Book with ISBN {isbn} not found")
            return False
        
        return member.return_book(book)
    
    def display_member_borrowed_books(self, member_id):
        """
        Display all books borrowed by a member.
        
        Args:
            member_id (str): Member ID
        """
        member = self.get_member(member_id)
        
        if not member:
            print(f"Member with ID {member_id} not found")
            return
        
        borrowed = member.get_borrowed_books()
        print(f"\n=== Books Borrowed by {member.name} ===")
        
        if not borrowed:
            print("No books borrowed")
            return
        
        for book in borrowed:
            print(f"- {book.title} (ISBN: {book.isbn})")
    
    def get_statistics(self):
        """Display library statistics."""
        total_books = len(self.__books)
        available_books = sum(1 for book in self.__books.values() if book.is_available())
        borrowed_books = total_books - available_books
        total_members = len(self.__members)
        
        print(f"\n=== {self.name} Statistics ===")
        print(f"Total Books: {total_books}")
        print(f"Available Books: {available_books}")
        print(f"Borrowed Books: {borrowed_books}")
        print(f"Total Members: {total_members}")
        print("-" * 40)
