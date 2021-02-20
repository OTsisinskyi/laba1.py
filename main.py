# Створити клас “Книжка” котрий містить поля:
# - кількість сторінок
# - автор книжки
# - ціна (в гривнях)

class Book:

    def __init__(self, author='', pages=0, price=0):
        self.author = author
        self.pages = pages
        self.price = price

    def print_out(self):
        return f"""\t\tAuthor of the book: {self.author} 
        Number of pages: {self.pages}
        The price of the book: {self.price} UAN\n"""


book_1 = Book("Brian Tracy", 106, 100)
print(book_1.print_out())

book_2 = Book("Taras Shevchenko", 405, 450)
print(book_2.print_out())

book_3 = Book("Ivan Franko", 237, 299)
print(book_3.print_out())
