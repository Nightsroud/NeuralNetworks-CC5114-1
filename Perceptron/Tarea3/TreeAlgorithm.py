from GenAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from Tarea3.Tree import tree
from random import *
import string
import time
import matplotlib.pyplot as plt

class TreeAlgorithm(GeneticAlgorithm):

    def __init__(self, sequence, size=2, k=750, N=1000, mutRate=0.01):
        self.digits = string.digits[1:]
        self.operators = '+-*/'
        super().__init__(sequence,  size, k, N, mutRate)

    def population(self, N, size):
        treelist = []
        for i in range(N):
            Tree = self.MakeTree(size)
            treelist.append(Tree)
        return treelist

    def MakeTree(self, size):
        if size > 0:
            arbolito = tree(choice(self.operators), self.MakeTree(size-1), self.MakeTree(size-1))
            return arbolito
        else:
            arbolito = tree(choice(self.digits))
            return arbolito

    def fitness(self, input):
        return input.evaluate()

    def tournament_selection(self, inputs, k):
        best = tree(0)
        for i in range(k):
            ind = inputs[randint(0, len(inputs) - 1)]
            if best.getValue() == 0 or (self.fitness(ind) > self.fitness(best)):
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
            paux = self.chooseTree(p1, p2)
            if random() < self.mutRate:
                paux.setValue(choice(self.operators))
            self.mutateLeafs(paux)
            newgen.append(paux)

        return newgen

    def chooseTree(self,p1,p2):
        if random() < 0.5:
            return self.replaceSide(p1,p2)
        else:
            return self.replaceSide(p2,p1)

    def replaceSide(self, pr, ps):
        if random() < 0.5:
            pa = pr.setLeft(self.selectSide(ps))
            return pa
        else:
            pb = pr.setRight(self.selectSide(ps))
            return pb

    def selectSide(self, ps):
        if random() < 0.5:
            return ps.getLeft()
        else:
            return ps.getRight()

    def mutateLeafs(self, pt):
        if pt.isLeaf():
            if random() < self.mutRate:
                pt.setValue(choice(self.digits))
        else:
            self.mutateLeafs(pt.getLeft())
            self.mutateLeafs(pt.getRight())

    def run(self, inputs, k):
        xgen = []
        ybest = []
        yprom = []
        runinputs = inputs
        breakcount = 0
        generacion = 0
        mejor = []
        fitmejor = 9999
        fitmax = self.sequence
        ti = time.time()
        while True:
            mejorb = mejor
            prom = 0
            print("Operando sobre Generacion: " + str(generacion))

            for i in runinputs:
                print(i.calculate())
                fit = self.fitness(i)
                prom += fit
                if abs(fit - fitmax) <= fitmejor:
                    mejor = i
                    fitmejor = fit
            prom /= len(runinputs)
            xgen.append(generacion)
            ybest.append(fitmejor)
            yprom.append(prom)

            if fitmax == fitmejor:
                print("Solucion encontrada en Generacion: " + str(generacion))
                print("Mejor: " + str(mejor.calculate()))
                break

            if mejorb == mejor:
                breakcount+=1
            else:
                breakcount = 0

            if breakcount == 100:
                print("Se llego al limite de 100 generaciones, solucion no encontrada.")
                break

            gen = self.reproduction(runinputs, k)
            generacion +=1
            runinputs = gen
            print("Fitness: "+str(fitmejor))
            print("Mejor: " +str(mejor.calculate()))
        tf = time.time()
        print("Tiempo de ejecucion: "+ str(tf - ti))
        plt.figure(1)
        plt.subplot(211)
        plt.xlabel("Generacion")
        plt.ylabel("Mejor por Generacion")
        plt.plot(xgen, ybest, 'b-')
        plt.subplot(212)
        plt.xlabel("Generacion")
        plt.ylabel("Promedio Fitness")
        plt.plot(xgen, yprom, 'r-')
        plt.show()

if __name__ == '__main__':
    TreeAlgorithm(5)
