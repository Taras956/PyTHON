from Book import Book
class PaperBook(Book):
    def __init__(self, title, publisher, author, year, genre, pageCount, widthInMm, heightInMm):
        super().__init__(title, publisher, author, year, genre)
        self.pageCount = pageCount
        self.widthInMm = widthInMm
        self.heightInMm = heightInMm

    pageCount = 400
    widthInMm =15
    heightInMm = 20

    def getPagesCount(self):
        return self.pageCount

    print("Кількість сторінок у книжці:", pageCount)
    print("Розмір книжки:", heightInMm, "на", widthInMm, "см")