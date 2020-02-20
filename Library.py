
class Library:
    def __init__ (self, id, books, signUpTime, booksSentPerDay):
        self.id = id
        self.books = books
        self.signUpTime = signUpTime
        self.booksSentPerDay = booksSentPerDay
    
    def getBooks(self):
        result = self.books[:self.booksSentPerDay - 1]
        self.books = self.books[self.booksSentPerDay:]
        return result