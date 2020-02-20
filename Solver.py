from Library import Library
from queue import Queue

class Solver:

    def __init__(self):
        self.datasets = ["a_example","b_read_on","c_incunabula","d_tough_choices","e_so_many_books","f_libraries_of_the_world"]


    def splitInts(self,inpStr):
        return [int(i) for i in inpStr.strip().split(" ")]

    def readFromFile(self,filename):
        with open(filename,"r") as inpFile:
            books, libraries, days = self.splitInts(inpFile.readline())
            bookValues = self.splitInts(inpFile.readline())
            #fuckin libs
            LibObjects = []
            for i in range(libraries):
                booksPerLib, signup, booksPerDay = self.splitInts(inpFile.readline())
                bookTypes = self.splitInts(inpFile.readline())

                LibObjects.append(Library(i,bookTypes,signup,booksPerDay))

        output = {}
        output["bookValues"] = bookValues
        output["days"] = days
        output["libs"] = LibObjects
        return output



    def writeToFile(self,filename,data):
        with open(filename,"w") as outFile:
            outFile.write(str(len(data["libOrder"]))+"\n")
            #out = ""
            #for lib in data["libOrder"]:
            #    out+=str(lib.id) + " "
            #outFile.write(out+"\n")
            for i in range(len(data["libOrder"])):
                out = ""
                out+=str(data["libOrder"][i].id) + " "

                out+=str(len(data["libBooks"][data["libOrder"][i].id])) + "\n"
                outFile.write(out)
                out = ""
                for a in data["libBooks"][data["libOrder"][i].id]:
                    out+=str(a)+" "
                outFile.write(out+"\n")

    def scoreOnDataset(self,data):
        bookList = data["libBooks"]
        bookValues = data["bookValues"]
        score=0
        booksDone = set()

        for list in bookList.values():
            for book in list:
                if book not in booksDone:
                    score += bookValues[book]
                    booksDone.add(book)

        return score

    def score(self):
        for setName in self.datasets:
            inputData = self.readFromFile(setName+".txt")
            output = self.solve2(inputData)
            print(f"Score on data set {setName}: {self.scoreOnDataset(output)}")
            self.writeToFile(setName+"output.txt",output)


    def solve(self,data):
        b=data["bookValues"]
        newLibs = sorted(data["libs"],key = lambda lib: lib.calculateWorth(b),reverse=True)
        output = {}
        done=set()
        output["libOrder"] = [lib for lib in newLibs]
        output["libBooks"] = {}

        for lib in data["libs"]:
            output["libBooks"][lib.id] = sorted(lib.books,key = lambda boi: data["bookValues"][boi] if boi not in done else 0,reverse=True)
            for book in output["libBooks"][lib.id]:
                done.add(book)
        output["bookValues"] = data["bookValues"]
        return output

    def solve2(self,data):
        b=data["bookValues"]
        output = {}
        done=set()

        libOrder = sorted(data["libs"],key = lambda lib: lib.calculateWorth(b,done))

        print(len(libOrder))
        output["libBooks"] = {}
        actualOrder=Queue()

        while len(libOrder)>0:
            lib=libOrder.pop()
            actualOrder.put(lib)
            output["libBooks"][lib.id] = sorted(lib.books,key = lambda boi: data["bookValues"][boi] if boi not in done else 0,reverse=True)
            for book in output["libBooks"][lib.id]:
                done.add(book)
            libOrder=sorted(libOrder,key = lambda lib: lib.calculateWorth(b,done))
            print(len(libOrder))

        output["libOrder"] = []

        while not actualOrder.empty():
            output["libOrder"].append(actualOrder.get())
        output["bookValues"] = data["bookValues"]
        return output

if __name__ == "__main__":
    solution = Solver()

    solution.score()
