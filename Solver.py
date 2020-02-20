class Solver:



    def __init__(self):
        self.datasets = []

    def readFromFile(self,filename):
        pass

    def writeToFile(self,filename):
        pass

    def score(self,):
        def scoreOnDataset():
            pass

        for setName in self.datasets:
            inputData = self.readFromFile(setName+".in")
            output = self.solve(inputData)
            print(f"Score on data set {setName}: {self.scoreOnDataset(output)}")
            self.writeToFile(setName+".txt")



    def solve(self):
        pass
