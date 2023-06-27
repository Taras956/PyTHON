class Book:
    def __init__(self, title, author, publisher, year, genre):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre

    def getAuthor(self):
        return self.author

    def getGenre(self):
        return self.genre

    def getTitle(self):
        return self.title

    def __str__(self):
        return f"Book: {self.title} by {self.author}, published by {self.publisher} ({self.year}), genre: {self.genre}"


class PaperBook(Book):
    def __init__(self, title, publisher, author, year, genre, pageCount, weight, price):
        super().__init__(title, author, publisher, year, genre)
        self.pageCount = pageCount
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"PaperBook: {super().__str__()}, pageCount: {self.pageCount}, weight: {self.weight}, price: {self.price}"


class ElectronicBook(Book):
    def __init__(self, title, publisher, author, year, genre, format, fileSize):
        super().__init__(title, author, publisher, year, genre)
        self.format = format
        self.fileSize = fileSize

    def __str__(self):
        return f"ElectronicBook: {super().__str__()}, format: {self.format}, fileSize: {self.fileSize}"
class BookNotFoundException(Exception):
    pass

import logging

def logged(exception, mode):
    logger = logging.getLogger("book_manager_logger")
    logger.setLevel(logging.INFO)

    if mode == "console":
        handler = logging.StreamHandler()
    elif mode == "file":
        handler = logging.FileHandler("book_manager.log")

    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger.exception(e)
        return wrapper
    return decorator

class BookManager:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    @logged(BookNotFoundException, "console")
    def searchByAuthor(self, author):
        result = []
        for book in self.books:
            if book.getAuthor() == author:
                result.append(book)
        if len(result) == 0:
            raise BookNotFoundException(f"No books found by author: {author}")
        return result

    @logged(BookNotFoundException, "file")
    
    def searchByGenre(self, genre):
        """ 
        ПЕРЕВІРКА НА ВИЙНЯТКИ.
        """

        print(self.searchByGenre.__doc__)
        pass
        result = []
        for book in self.books:
            if book.getGenre() == genre:
                result.append(book)
        if len(result) == 0:
            raise BookNotFoundException(f"No books found in genre: {genre}")
        return result


books = []
books.append(PaperBook("Harry Potter", "Lviv tratata", "T.Tupytsia", 2036, "Romantic", 349, 150, 228))
books.append(ElectronicBook("Harry Potter", "Lviv tratata", "T.Tupytsia", 2036, "Romantic", "PDF", 1024 * 1024))

for book in books:
    print(book)

bookManager = BookManager()
book1 = Book("Harry Potter", "J.K. Rowling", "Bloomsbury Publishing", 1997, "Fantasy")
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", "George Allen & Unwin", 1954, "Fantasy")
bookManager.addBook(book1)
bookManager.addBook(book2)
booksByAuthor = bookManager.searchByAuthor("J.K. Rowling")
booksByGenre = bookManager.searchByGenre("Fantasy")

for book in booksByAuthor:
    print(f"{book.getTitle()} by {book.getAuthor()}")

for book in booksByGenre:
    print(f"{book.getTitle()} is a {book.getGenre()} book")
