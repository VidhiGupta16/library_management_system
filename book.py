"""
Book class with encapsulation for book availability.
Demonstrates encapsulation OOP concept.
"""


class Book:
    """Represents a book in the library with encapsulated availability status."""
    
    def __init__(self, title, author, isbn):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            isbn (str): The ISBN number of the book
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True  # Private attribute (encapsulation)
    
    def is_available(self):
        """
        Check if the book is available for borrowing.
        
        Returns:
            bool: True if available, False otherwise
        """
        return self.__available
    
    def borrow(self):
        """
        Mark the book as borrowed.
        
        Returns:
            bool: True if successfully borrowed, False if already borrowed
        """
        if self.__available:
            self.__available = False
            return True
        return False
    
    def return_book(self):
        """
        Mark the book as returned.
        
        Returns:
            bool: True if successfully returned, False if already available
        """
        if not self.__available:
            self.__available = True
            return True
        return False
    
    def display_info(self):
        """Display book information."""
        status = "Available" if self.__available else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")
        print("-" * 40)
    
    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.__available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"
