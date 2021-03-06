from GenAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from random import *
import string

class sGeneticAlgorithm(GeneticAlgorithm):

    def __init__(self, sequence, size=3, k=750, N=1000, mutRate=0.01):
        self.strings = string.ascii_lowercase
        super().__init__(sequence,  size, k, N, mutRate)

    def population(self, N, size):
        strlist = []
        for i in range(N):
            s = []
            for j in range(size):
                s.append(choice(self.strings))
            strlist.append(s)
        return strlist

    def reproduction(self, inputs, k):
        parents = []
        for i in range(2*len(inputs)):
            parents.append(self.tournament_selection(inputs, k))

        newgen = []
        while len(parents) != 0:
            p1 = parents.pop(0)
            p2 = parents.pop(0)
            mixpoint = randint(0, len(p1) - 1)
            paux = p1[0:mixpoint] + p2[mixpoint:]
            for i in range(len(p1)):
                if random() < self.mutRate:
                    paux[i] = choice(self.strings)
            newgen.append(paux)
            shuffle(newgen)
            return newgen

if __name__ == '__main__':
    sGeneticAlgorithm(['c', 'a', 't'])