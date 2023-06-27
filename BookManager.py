class Book:
    def __init__(self, title, author, publisher, year, genre):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}, Genre: {self.genre}"


class PaperBook(Book):
    def __init__(self, title, author, publisher, year, genre, pageCount, weight, isbn):
        super().__init__(title, author, publisher, year, genre)
        self.page_count = pageCount
        self.weight = weight
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}, Genre: {self.genre}, Page Count: {self.page_count}, Weight: {self.weight}, ISBN: {self.isbn}"


class ElectronicBook(Book):
    def __init__(self, title, author, publisher, year, genre, format, fileSize):
        super().__init__(title, author, publisher, year, genre)
        self.format = format
        self.file_size = fileSize

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}, Genre: {self.genre}, Format: {self.format}, File Size: {self.file_size}"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        result = []
        for book in self.books:
            if book.get_author() == author:
                result.append(book)
        return result

    def search_by_genre(self, genre):
        result = []
        for book in self.books:
            if book.get_genre() == genre:
                result.append(book)
        return result


books = []
books.append(PaperBook("Harry Poter", "Lviv tratata", "T.Tupytsia", 2036, "Romantic", 349, 150, 228))
books.append(ElectronicBook("Harry Poter", "Lviv tratata", "T.Tupytsia", 2036, "Romantic", "PDF", 1024 * 1024))

for book in books:
    print(book)

book_manager = BookManager()
book1 = Book("Harry Potter", "J.K. Rowling", "Bloomsbury Publishing", 1997, "Fantasy")
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", "George Allen & Unwin", 1954, "Fantasy")
book_manager.add_book(book1)
book_manager.add_book(book2)

books_by_author = book_manager.search_by_author("J.K. Rowling")
books_by_genre = book_manager.search_by_genre("Fantasy")

for book in books_by_author:
    print(book.get_title(), "by", book.get_author())

for book in books_by_genre:
    print(book.get_title(), "is a", book.get_genre(), "book")
