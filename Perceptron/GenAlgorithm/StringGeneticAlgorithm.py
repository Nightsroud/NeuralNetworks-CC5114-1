from GenAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from random import *
import string

class sGeneticAlgorithm(GeneticAlgorithm):

    def __init__(self, sequence, k=20, N=40, size=3, mutRate=0.01):
        self.strings = string.ascii_lowercase
        super().__init__(sequence, k, N, size, mutRate)

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
        for i in range(len(inputs) * 2):
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

            return newgen

if __name__ == '__main__':
    sGeneticAlgorithm(['c', 'a', 't'])