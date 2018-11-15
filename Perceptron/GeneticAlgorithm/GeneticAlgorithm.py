from random import *

class GeneticAlgorithm:

    def __init__(self, N, nBits, sequence, mixingPoint, mutRate=0.01):
        self.N = N
        self.sequence = sequence
        self.mixingPoint = mixingPoint
        self.mutRate = mutRate
        self.pop = self.population(self.N, nBits)


    def population(self, N, nBits):
        bitlist = []
        for i in range(N):
            bit =[]
            for j in range(nBits):
                bit.append(randint(0, 1))
            bitlist.append(bit)
        return bitlist

    def fitness(self, input):
        assert len(input) == len(self.sequence)
        count = 0
        for i in range(len(input)):
            if input[i] == self.sequence[i]:
                count+=1
        return count

    def tournament_selection(self, inputs, k):
        best = []
        for i in range(k):
            ind = inputs[randint(0, len(inputs) - 1)]
            if len(best) == 0 or (self.fitness(ind) > self.fitness(best)):
                best = ind
        return best

    def reproduction(self, inputs, k):

        parents  = []
        for i in range(len(inputs)*2):
            parents.append(self.tournament_selection(inputs, k))

        newgen = []
        while len(parents) != 0:
            p1 = parents.pop(0)
            p2 = parents.pop(0)
            mixpoint = randint(0, len(p1) - 1)
            paux = p1[0:mixpoint]+p2[mixpoint:]
            for i in range(len(p1)):
                if random() < self.mutRate:
                    paux[i] = randint(0, 1)
            newgen.append(paux)

        return newgen

    def run(self, inputs, k):
        runinputs = inputs
        breakcount = 0
        generacion = 0
        mejor = []
        fitmejor = 0
        fitmax = self.fitness(self.sequence)
        print("Operando sobre Generacion: "+ str(generacion))
        while True:
            for i in inputs:
                if self.fitness(i) > fitmejor:
                    mejor = i
                    fitmejor = self.fitness(i)
            if fitmax == fitmejor:
                print("Solucion encontrada en Generacion: " + str(generacion))
                print("Mejor: " + str(mejor))
            gen = self.reproduction(inputs, k)