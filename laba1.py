class Book:
    __count = 0

    def __init__(self, author='', name='', rating=0, pages=0, price=0):
        Book.__count += 1
        self.rating = rating
        self.author = author
        self.pages = pages
        self.price = price
        self.name = name

    def __str__(self):
        return f"""\t\tAuthor of the book: {self.author}
        Book title: {self.name}
        Book evaluation: {self.rating}
        Number of pages: {self.pages}
        The price of the book: {self.price} UAN\n"""

    @staticmethod
    def get_count():
        return Book.__count

    def __repr__(self):
        return f"The object Book - {self.author}"

    def __del__(self):
        print('деструктор')


book_1 = Book("Brian Tracy", "Do it now", 9.5, 106, 100)
print(book_1.__str__())

book_2 = Book("Taras Shevchenko", "Kobzar", 8.2, 405, 450)
print(book_2.__str__())

book_3 = Book("Ivan Franko", "Stonemason", 6.9, 237, 299)
print(book_3.__str__())

print(Book.get_count())
