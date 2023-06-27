from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author, publisher, year, genre):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.options = set()

    def __iter__(self):
        return iter(self.options)

    @abstractmethod
    def getPagesCount(self):
        pass


class PaperBook(Book):
    def __init__(self, title, author, publisher, year, genre, count_in_warehouse):
        super().__init__(title, author, publisher, year, genre)
        self.count_in_warehouse = count_in_warehouse
        self.options = {"з товстою обкладинкою"}

    def getPagesCount(self):
        return 100


class ElectronicBook(Book):
    def __init__(self, title, author, publisher, year, genre, count_in_warehouse):
        super().__init__(title, author, publisher, year, genre)
        self.count_in_warehouse = count_in_warehouse
        self.options = {"pdf"}

    def getPagesCount(self):
        return 200


class RegularManager:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def __iter__(self):
        return iter(self.books)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]


class SetManager:
    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    def __iter__(self):
        return self._iterate_set()

    def __len__(self):
        return self._calculate_set_length()

    def __getitem__(self, index):
        return self._get_item_from_set(index)

    def _iterate_set(self):
        for book in self.regular_manager:
            for item in book:
                yield item

    def _calculate_set_length(self):
        length = 0
        for book in self.regular_manager:
            if isinstance(book, Book):
                length += len(book.options)
        return length

    def _get_item_from_set(self, index):
        count = 0
        for book in self.regular_manager:
            book_set = book.options
            set_length = len(book_set)
            if index < count + set_length:
                return list(book_set)[index - count]
            count += set_length


# Example usage:
regular_manager = RegularManager()
regular_manager.addBook(PaperBook("Harry Potter", "J.K. Rowling", "Bloomsbury Publishing", 1997, "Fantasy", 10))
regular_manager.addBook(ElectronicBook("The Lord of the Rings", "J.R.R. Tolkien", "George Allen & Unwin", 1954, "Fantasy", 5))

set_manager = SetManager(regular_manager)

print(f"Set Manager Length: {len(set_manager)}")

for item in set_manager:
    print(item)