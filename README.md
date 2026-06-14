# Library Management System - OOP Project

A complete Library Management System demonstrating Object-Oriented Programming (OOP) concepts in Python.

## Project Overview

This project implements a library management system using core OOP principles:
- **Encapsulation**: Private attributes for book availability and borrowed books
- **Inheritance**: Member types (Student, Faculty, Researcher) inherit from base Member class
- **Polymorphism**: Different borrowing rules for different member types
- **Duck Typing**: Notification system that works with any notification type

## Project Structure

```
python_project/
├── book.py          # Book class with encapsulation
├── member.py        # Member classes with inheritance
├── library.py       # Library management system
├── main.py          # Demo script
└── README.md        # This file
```

## File Descriptions

### book.py
Contains the `Book` class that demonstrates encapsulation:
- Private `__available` attribute to track book status
- Methods to borrow and return books with validation
- Public interface for accessing book information

### member.py
Contains member classes demonstrating inheritance and polymorphism:
- `Member`: Base class with common member functionality
- `Student`: Inherits from Member, 3 books max, 14-day loan
- `Faculty`: Inherits from Member, 10 books max, 30-day loan
- `Researcher`: Inherits from Member, 15 books max, 60-day loan

### library.py
Contains the `Library` class that integrates everything:
- Manages books and members
- Handles borrowing and returning operations
- Provides statistics and reporting

### main.py
Demo script that demonstrates all OOP concepts:
- Creates library, books, and members
- Shows encapsulation in action
- Demonstrates polymorphism with different member types
- Includes duck typing example with notifications

## OOP Concepts Demonstrated

### 1. Encapsulation
- Private attributes using double underscore (`__available`, `__borrowed_books`)
- Public methods to access and modify private data
- Data hiding and validation

### 2. Inheritance
- `Student`, `Faculty`, and `Researcher` inherit from `Member`
- Code reuse through inheritance
- `super()` used to call parent class methods

### 3. Polymorphism
- `get_max_books()` returns different values for different member types
- `get_loan_period()` returns different values for different member types
- `display_info()` behaves differently for each member type

### 4. Duck Typing
- Notification system works with any object that has a `send()` method
- "If it walks like a duck and quacks like a duck, it's a duck"

## How to Run

1. Navigate to the project directory:
```bash
cd "c:\Users\DELL\OneDrive\New folder\python_project"
```

2. Run the demo script:
```bash
python main.py
```

## Example Output

The demo script will:
- Create a library with books
- Add different types of members (Student, Faculty, Researcher)
- Demonstrate borrowing with different limits
- Show book availability changes
- Display library statistics
- Demonstrate duck typing with notifications

## Key Features

### Book Management
- Add books with title, author, and ISBN
- Track book availability (encapsulated)
- Borrow and return operations with validation

### Member Management
- Different member types with different privileges
- Inheritance hierarchy for code reuse
- Polymorphic behavior for borrowing rules

### Library Operations
- List all books and available books
- Process borrow and return requests
- View member's borrowed books
- Generate library statistics

## Practice Tasks Included

The project includes practice tasks from the training guide:
1. **Book class**: Attributes (title, author, price) with display_details()
2. **Student class**: Private `__marks` with validation (0-100)
3. **Inheritance hierarchy**: Person → Employee → Manager
4. **Polymorphism**: Shape → Circle, Rectangle with area() method
5. **Duck typing**: PDFReport, ExcelReport, CSVReport with generate()

## Extension Ideas

- Add due date tracking and late fees
- Implement book reservations
- Add search functionality for books and members
- Create a GUI interface
- Add database persistence
- Implement book categories and genres

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Author

Created as part of Python OOP Hands-On Training Guide
