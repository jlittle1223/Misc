import random
import math


# Number of Generations
numGenerations = 100


# Proportion of the initial distribution that has gene X
X_initial_distribution = 0.99

# r0 = average number of children
r0_X = 0.99
r0_Y = 1.05





class Organism():
    def __init__(self, name:str, gene:str):
        self.name = name
        self.gene = gene

        if self.gene == "X":
            self.r0 = r0_X
        elif self.gene == "Y":
            self.r0 = r0_Y


    # returns number of children
    def reproduce(self) -> int:
        minChildren = math.floor(self.r0)
        
        randNum = random.random()
        if randNum <= self.r0 - minChildren:
            return minChildren + 1
        return minChildren
            


def createGene(probability_X:float) -> " 'X' or 'Y' ":
    randNum = random.random()
    if randNum <= probability_X:
        return "X"
    return "Y"



def createGenePool(populationSize:int) -> "list of organisms":
    genePool = []
    for i in range(populationSize):
        gene = createGene(X_initial_distribution)
        
        organism = Organism("org_" + str(i), gene)
        genePool.append(organism)

    return genePool


def showGenePool(genePool:list) -> None:
    total_X = 0
    total_Y = 0
    for organism in genePool:
        #print(organism.name, organism.gene)
        if organism.gene == "X":
            total_X += 1
        elif organism.gene == "Y":
            total_Y += 1

    proportion_X = float(total_X) / float(len(genePool))
    proportion_Y = float(total_Y) / float(len(genePool))
    print("proportion of X = {0:.2%}".format(proportion_X))
    print("proportion of Y = {0:.2%}".format(proportion_Y))


def evolve(genePool:list) -> "list of organisms in next generation":
    newGenePool = []
    i = 0
    for organism in genePool:
        for j in range(organism.reproduce()):
            baby = Organism("org_" + str(i), organism.gene)
            newGenePool.append(baby)
        i += 1
    return newGenePool
        



if __name__ == "__main__":
    genePool = createGenePool(1000)
    showGenePool(genePool)
    for i in range(numGenerations):
        genePool = evolve(genePool)
        print("Generation: {}   Size: {}".format(i + 1, len(genePool)))
        showGenePool(genePool)
    
    






