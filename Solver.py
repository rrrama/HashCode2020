class Solver:



    def __init__(self):
        self.datasets = ["a_example","b_read_on","c_incunabula","d_tough_choices","e_so_many_books","f_libraries_of_the_world"]


    def splitInts(self,inpStr):
        return [int(i) for i in inpStr.strip().split(" ")]

    def readFromFile(self,filename):
        with open(filename) as inpFile:


    def writeToFile(self,filename):
        pass

    def score(self,):
        def scoreOnDataset():
            pass

        for setName in self.datasets:
            inputData = self.readFromFile(setName+".txt")
            output = self.solve(inputData)
            print(f"Score on data set {setName}: {self.scoreOnDataset(output)}")
            self.writeToFile(setName+"output.txt")



    def solve(self):
        pass
