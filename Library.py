
class Library:
    def __init__ (self, id, books, signUpTime, booksSentPerDay):
        self.id = id
        self.books = books
        self.signUpTime = signUpTime
        self.booksSentPerDay = booksSentPerDay
        self.numDone=0
    
    def getBooks(self):
        result = self.books[:self.booksSentPerDay - 1]
        self.books = self.books[self.booksSentPerDay:]
        return result

    def scanBooks():
        lis = []
        i = 0
        pointer = self.numDone
        while (i<self.booksSentPerDay):
            lis.append(self.books[pointer])
            i=i+1
            pointer=pointer+1
        self.numDone=self.numDone+1
        return lis
