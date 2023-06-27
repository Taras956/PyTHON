from Book import Book
class ElectronicBook(Book):
    def __init__(self, title, publisher, author, year, genre, format, fileSizeInBytes):
        super().__init__(title, publisher, author, year, genre)
        self.format = format
        self.fileSizeInBytes = fileSizeInBytes
        self.BYTES_PER_PAGE_COUNT = 1024

    def getPagesCount(self):
        return int(self.fileSizeInBytes / self.BYTES_PER_PAGE_COUNT)