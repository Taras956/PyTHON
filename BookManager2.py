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


class BookManager:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]

    def __iter__(self):
        return iter(self.books)

    def perform_method(self, method):
        return [getattr(book, method)() for book in self.books]

    def enumerate_objects(self):
        return [(index, obj) for index, obj in enumerate(self.books)]

    def zip_results(self, method):
        return [(obj, getattr(obj, method)()) for obj in self.books]

    def get_attributes_by_type(self, data_type):
        return {key: value for book in self.books for key, value in book.__dict__.items() if isinstance(value, data_type)}

    def check_conditions(self, condition):
        return {"all": all(condition(book) for book in self.books), "any": any(condition(book) for book in self.books)}

    def searchByAuthor(self, author):
        result = []
        for book in self.books:
            if book.getAuthor() == author:
                result.append(book)
        return result

    def searchByGenre(self, genre):
        result = []
        for book in self.books:
            if book.getGenre() == genre:
                result.append(book)
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


authors = bookManager.perform_method("getAuthor")
print(authors)


enumerated_objects = bookManager.enumerate_objects()
for index, obj in enumerated_objects:
    print(f"Index: {index}, Object: {obj}")


results = bookManager.zip_results("getAuthor")
for obj, result in results:
    print(f"Object: {obj}, Result: {result}")


attributes = bookManager.get_attributes_by_type(int)
print(attributes)


def is_fantasy(book):
    return book.getGenre() == "Fantasy"

conditions = bookManager.check_conditions(is_fantasy)
print(conditions)