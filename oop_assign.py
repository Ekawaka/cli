#Create a simple Object-Oriented Program (OOP) that simulates a basic library management system. 
#This system will manage books and allow users to check out and return books. Create a Book class

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
    
    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False
    
    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, isbn: {self.isbn}")
    
myBook = Book("Harry potter", "Rowling", 13)


print(myBook.title)
print(myBook.author)
print(myBook.isbn)

