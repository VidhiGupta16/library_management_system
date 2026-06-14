"""
Library Management System - Demo Script
Demonstrates all OOP concepts: Encapsulation, Inheritance, Polymorphism, Duck Typing
"""

from library import Library
from member import Student, Faculty, Researcher


def main():
    """Main function to demonstrate the Library Management System."""
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - OOP DEMONSTRATION")
    print("=" * 60)
    
    # Create library
    library = Library("Central Library")
    print(f"\nCreated: {library.name}")
    
    # Add books to the library
    print("\n--- Adding Books ---")
    book1 = library.add_book("Python Programming", "John Smith", "ISBN001")
    book2 = library.add_book("Data Structures", "Jane Doe", "ISBN002")
    book3 = library.add_book("Algorithms", "Bob Johnson", "ISBN003")
    book4 = library.add_book("Machine Learning", "Alice Williams", "ISBN004")
    book5 = library.add_book("Web Development", "Charlie Brown", "ISBN005")
    book6 = library.add_book("Database Systems", "Diana Prince", "ISBN006")
    
    # Add members with different types (Inheritance)
    print("\n--- Adding Members (Inheritance) ---")
    student1 = Student("Alice", "STU001", "S1001")
    student2 = Student("Bob", "STU002", "S1002")
    faculty1 = Faculty("Dr. Smith", "FAC001", "Computer Science")
    faculty2 = Faculty("Dr. Johnson", "FAC002", "Mathematics")
    researcher1 = Researcher("Dr. Williams", "RES001", "Artificial Intelligence")
    
    library.add_member(student1)
    library.add_member(student2)
    library.add_member(faculty1)
    library.add_member(faculty2)
    library.add_member(researcher1)
    
    # Display all members (Polymorphism - different display_info behavior)
    print("\n--- Member Information (Polymorphism) ---")
    library.list_all_members()
    
    # Display all books
    print("\n--- All Books ---")
    library.list_all_books()
    
    # Demonstrate Encapsulation - book availability
    print("\n--- Encapsulation: Book Availability ---")
    print(f"Book '{book1.title}' available: {book1.is_available()}")
    
    # Demonstrate Polymorphism - different borrowing rules
    print("\n--- Polymorphism: Different Borrowing Rules ---")
    print(f"Student max books: {student1.get_max_books()}, Loan period: {student1.get_loan_period()} days")
    print(f"Faculty max books: {faculty1.get_max_books()}, Loan period: {faculty1.get_loan_period()} days")
    print(f"Researcher max books: {researcher1.get_max_books()}, Loan period: {researcher1.get_loan_period()} days")
    
    # Borrow books - Student
    print("\n--- Student Borrowing Books ---")
    library.process_borrow("STU001", "ISBN001")
    library.process_borrow("STU001", "ISBN002")
    library.process_borrow("STU001", "ISBN003")
    library.process_borrow("STU001", "ISBN004")  # Should fail - limit reached
    
    # Display student's borrowed books
    library.display_member_borrowed_books("STU001")
    
    # Borrow books - Faculty (can borrow more)
    print("\n--- Faculty Borrowing Books ---")
    library.process_borrow("FAC001", "ISBN004")
    library.process_borrow("FAC001", "ISBN005")
    library.process_borrow("FAC001", "ISBN006")
    
    # Display faculty's borrowed books
    library.display_member_borrowed_books("FAC001")
    
    # Display available books
    print("\n--- Available Books After Borrowing ---")
    library.list_available_books()
    
    # Return books
    print("\n--- Returning Books ---")
    library.process_return("STU001", "ISBN001")
    library.process_return("STU001", "ISBN002")
    
    # Display available books after return
    print("\n--- Available Books After Return ---")
    library.list_available_books()
    
    # Display statistics
    library.get_statistics()
    
    # Demonstrate Duck Typing
    print("\n--- Duck Typing Demonstration ---")
    
    class EmailNotification:
        def send(self, message):
            print(f"Email: {message}")
    
    class SMSNotification:
        def send(self, message):
            print(f"SMS: {message}")
    
    class PushNotification:
        def send(self, message):
            print(f"Push: {message}")
    
    def send_notification(notification, message):
        """Duck typing - works with any object that has send() method"""
        notification.send(message)
    
    send_notification(EmailNotification(), "Book is due tomorrow")
    send_notification(SMSNotification(), "Book is due tomorrow")
    send_notification(PushNotification(), "Book is due tomorrow")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nOOP Concepts Demonstrated:")
    print("1. Encapsulation: Private __available and __borrowed_books attributes")
    print("2. Inheritance: Student, Faculty, Researcher inherit from Member")
    print("3. Polymorphism: get_max_books() and get_loan_period() behave differently")
    print("4. Duck Typing: send_notification() works with any notification type")
    print("5. Abstraction: Complex operations hidden behind simple methods")


if __name__ == "__main__":
    main()
