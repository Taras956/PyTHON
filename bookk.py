class Book:
    def __init__(self, title, author, publisher, year, genre, count_in_warehouse):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.count_in_warehouse = count_in_warehouse

    def get_book(self, quantity):
        if self.count_in_warehouse >= quantity:
            self.count_in_warehouse -= quantity
            return quantity
        else:
            available = self.count_in_warehouse
            self.count_in_warehouse = 0
            return available

    def has_more_books(self):
        return self.count_in_warehouse > 0

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

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_year(self, year):
        self.year = year

    def set_genre(self, genre):
        self.genre = genre

    def set_count_in_warehouse(self, count_in_warehouse):
        self.count_in_warehouse = count_in_warehouse


book = Book("Harry Poter", "T.Tupytsia", "Lviv tratata", 2036, "Romantic", 20)
print(book.get_book(7))
print(book.has_more_books())
print(book.get_book(10))
print(book.has_more_books())