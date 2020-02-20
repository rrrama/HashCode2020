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

        return bookValues,days,LibObjects



    def writeToFile(self,filename,data):
        with open(filename,"w") as outFile:
            outFile.write(str(len(data))+"\n")
            out = ""
            for lib in data:
                out+=lib.id + " "
            outFile.write(out+"\n")


    def score(self,):
        def scoreOnDataset(inputData, order):
            books,days,LibObjects = inputData
            

        for setName in self.datasets:
            inputData = self.readFromFile(setName+".txt")
            output = self.solve(inputData)
            print(f"Score on data set {setName}: {self.scoreOnDataset(inputData,output)}")
            self.writeToFile(setName+"output.txt")



    def solve(self):
        pass
