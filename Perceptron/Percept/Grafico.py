from Percept.Perceptrons import *
from random import *


class Graficar:

    def __init__(self):
        self.x = 0
        self.xcoor = []
        self.ycoord = []
        self.recta = 7*self.x + 5
        self.randWeights = [uniform(-2, 2), uniform(-2, 2)]
        self.randBias =  uniform(-2, 2)
        self.percptron = Perceptron(self.randWeights, self.randBias)
        #for i in range(0, 200):
            #self.
