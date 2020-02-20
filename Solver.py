from Library import Library

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
                booksPerLib, signup, booksPerDay = self.splitInts(inp.realine())
                bookTypes = self.splitInts(inp.realine())

                LibObjects.append(Library(i,bookTypes,signup,booksPerDay))

        output = {}
        output["bookValues"] = bookValues
        output["days"] = days
        output["libs"] = LibObjects
        return output



    def writeToFile(self,filename,data):
        with open(filename,"w") as outFile:
            outFile.write(str(len(data))+"\n")
            out = ""
            for lib in data:
                out+=lib.id + " "
            outFile.write(out+"\n")
            for i in range(len(data["libOrder"])):
                out = ""
                out+=str(data["libOrder"][i].id) + " "
                out+=str(len(data["libBooks"][i])) + "\n"
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
            output = self.solve(inputData)
            print(f"Score on data set {setName}: {self.scoreOnDataset(output)}")
            self.writeToFile(setName+"output.txt")



    def solve(self,data):
        newLibs = sorted(data["libs"],key = lambda boi: boi.signUpTime)
        output = {}
        output["libOrder"] = [boi.id for boi in data["libs"]]
        output["libBooks"] = {boi.id:boi.books for boi in data["libs"]}
        output["bookValues"] = data["bookValues"]
        return output

if __name__ == "__main__":
    solution = Solver()

    D = {"libOrder": [1,0], "libBooks": {0:[1,4],1:[0,2,3,5]},"bookValues": [1, 2, 3, 6, 5, 4]}
    print(solution.scoreOnDataset(D))
