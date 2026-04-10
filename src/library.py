class Library:
    def __init__(self):
        self.books = []

    def add_books(self, books):
        self.books = books

    def search_by_title(self, title):
        results = []

        for book in self.books:
            if book["title"] == title:
                results.append(book)

        return results

    def search_by_author(self, author):
        results = []

        for book in self.books:
            if book["author"] == author:
                results.append(book)

        return results

    def borrow_book(self, title):
        for book in self.books:
            if book["title"] == title:
                book["borrowed"] = True
                return

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title:
                book["borrowed"] = False
                return

    def is_book_borrowed(self, title):
        for book in self.books:
            if book["title"] == title:
                return book["borrowed"]