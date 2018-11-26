from GenAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from random import *

class QueenGeneticAlgorithm(GeneticAlgorithm):

    def __init__(self, sequence, k=75, N=100, size=4, mutRate=0.01):
        super().__init__(sequence, k, N, size, mutRate)

    def population(self, N, size):
        queenlist = []
        for i in range(N):
            queen = []
            for j in range(size):
                queen.append(randint(0, size - 1))
            queenlist.append(queen)
        return queenlist

    def fitness(self, input):
        assert len(input) == len(self.sequence)
        count = len(input)
        for i in range(len(input)):
            fila = i
            columna = input[i]
            count -= self.canAttackColumna(fila, columna, input)
            count -= self.canAttackDiagonal(fila, columna, input)
        return count

    def canAttackColumna(self, fila, columna, input):
        cont = 0
        foundcol = False
        for j in range(len(input)):
            if j <= fila:
                continue
            if columna == input[j] and foundcol is False:
                cont +=1
                foundcol = True
        return cont

    def canAttackDiagonal(self, fila, columna, input):
        sumcount = 1
        conta = 0
        founddiag1 = False
        founddiag2 = False
        for k in range(len(input)):
            if k <= fila:
                continue
            if (columna + sumcount) == input[k] and founddiag1 is False:
                conta += 1
                founddiag1 = True
            if (columna - sumcount) == input[k] and founddiag2 is False:
                conta += 1
                founddiag2 = True
            sumcount += 1
        return conta

if __name__ == '__main__':
    QueenGeneticAlgorithm([1, 3, 0, 2])