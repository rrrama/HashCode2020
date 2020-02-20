
class Library:
    def __init__ (self, id, books, signUpTime, booksSentPerDay):
        self.id = id
        self.books = books
        self.signUpTime = signUpTime
        self.booksSentPerDay = booksSentPerDay
        self.numDone=0

    def getTotalBookValue(self,bookValues):
        b = 0
        for book in self.books:
            b += bookValues[book]
        return b

    def scanBooks(self):
        lis = []
        i = 0
        pointer = self.numDone
        while (i<self.booksSentPerDay):
            lis.append(self.books[pointer])
            i=i+1
            pointer=pointer+1
        self.numDone=self.numDone+self.booksSentPerDay
        return lis

    def calculateWorth(self,bookValues):
        totalBookValue = self.getTotalBookValue(bookValues)
        return totalBookValue/(self.booksSentPerDay*self.signUpTime)
