"""
Member classes demonstrating inheritance and polymorphism.
Base Member class and derived classes for different member types.
"""


class Member:
    """Base class for library members."""
    
    def __init__(self, name, member_id):
        """
        Initialize a Member object.
        
        Args:
            name (str): Name of the member
            member_id (str): Unique member ID
        """
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []  # Private list (encapsulation)
    
    def get_max_books(self):
        """
        Get the maximum number of books this member can borrow.
        To be overridden by derived classes (polymorphism).
        
        Returns:
            int: Maximum number of books
        """
        return 3  # Default for regular members
    
    def get_loan_period(self):
        """
        Get the loan period in days for this member.
        To be overridden by derived classes (polymorphism).
        
        Returns:
            int: Loan period in days
        """
        return 14  # Default 14 days for regular members
    
    def borrow_book(self, book):
        """
        Borrow a book from the library.
        
        Args:
            book (Book): The book to borrow
            
        Returns:
            bool: True if successful, False otherwise
        """
        if len(self.__borrowed_books) >= self.get_max_books():
            print(f"{self.name} has reached maximum borrowing limit ({self.get_max_books()})")
            return False
        
        if book.borrow():
            self.__borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        else:
            print(f"Book '{book.title}' is not available")
            return False
    
    def return_book(self, book):
        """
        Return a book to the library.
        
        Args:
            book (Book): The book to return
            
        Returns:
            bool: True if successful, False otherwise
        """
        if book in self.__borrowed_books:
            if book.return_book():
                self.__borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'")
                return True
        print(f"{self.name} does not have '{book.title}' borrowed")
        return False
    
    def get_borrowed_books(self):
        """
        Get list of borrowed books.
        
        Returns:
            list: List of borrowed Book objects
        """
        return self.__borrowed_books.copy()
    
    def display_info(self):
        """Display member information."""
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print(f"Max Books: {self.get_max_books()}")
        print(f"Loan Period: {self.get_loan_period()} days")
        print(f"Books Borrowed: {len(self.__borrowed_books)}")
        print("-" * 40)


class Student(Member):
    """Student member with specific borrowing rules."""
    
    def __init__(self, name, member_id, student_id):
        """
        Initialize a Student member.
        
        Args:
            name (str): Name of the student
            member_id (str): Unique member ID
            student_id (str): Student ID number
        """
        super().__init__(name, member_id)
        self.student_id = student_id
    
    def get_max_books(self):
        """Students can borrow up to 3 books."""
        return 3
    
    def get_loan_period(self):
        """Students have 14-day loan period."""
        return 14
    
    def display_info(self):
        """Display student information."""
        print(f"--- Student Member ---")
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Faculty(Member):
    """Faculty member with extended borrowing privileges."""
    
    def __init__(self, name, member_id, department):
        """
        Initialize a Faculty member.
        
        Args:
            name (str): Name of the faculty
            member_id (str): Unique member ID
            department (str): Department name
        """
        super().__init__(name, member_id)
        self.department = department
    
    def get_max_books(self):
        """Faculty can borrow up to 10 books."""
        return 10
    
    def get_loan_period(self):
        """Faculty have 30-day loan period."""
        return 30
    
    def display_info(self):
        """Display faculty information."""
        print(f"--- Faculty Member ---")
        super().display_info()
        print(f"Department: {self.department}")


class Researcher(Member):
    """Researcher member with special borrowing privileges."""
    
    def __init__(self, name, member_id, research_area):
        """
        Initialize a Researcher member.
        
        Args:
            name (str): Name of the researcher
            member_id (str): Unique member ID
            research_area (str): Area of research
        """
        super().__init__(name, member_id)
        self.research_area = research_area
    
    def get_max_books(self):
        """Researchers can borrow up to 15 books."""
        return 15
    
    def get_loan_period(self):
        """Researchers have 60-day loan period."""
        return 60
    
    def display_info(self):
        """Display researcher information."""
        print(f"--- Researcher Member ---")
        super().display_info()
        print(f"Research Area: {self.research_area}")
