from Percept.Perceptrons import *
from math import *
from random import *

class Sigmoid(Perceptron):

    def __init__(self, weights, bias):
        super().__init__(weights, bias)

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        r = 0
        for x in range(len(inputs)):
            r += self.weight[x] * inputs[x]
        r += self.bias
        r2 = 1/(1 + exp(- r))
        return r2

class sAND(Sigmoid):

    def __init__(self):
        super().__init__([1.0, 1.0], -1.5)
        self.andTraining()

    def andTraining(self, trainInputs=100):
        inputs = []
        for i in range(trainInputs):
            par = [randint(0, 1), randint(0, 1)]
            inputs.append(par)
        for j in range(len(inputs)):
            if pAND().feed(inputs[j]):
                self.pretraining(inputs[j], 1)
            else:
                self.pretraining(inputs[j], 0)


class sOR(Sigmoid):

    def __init__(self):
        super().__init__([1.0, 1.0], -0.5)
        self.orTraining()

    def orTraining(self, trainInputs=100):
        inputs = []
        for i in range(trainInputs):
            par = [randint(0, 1), randint(0, 1)]
            inputs.append(par)
        for j in range(len(inputs)):
            if pOR().feed(inputs[j]):
                self.pretraining(inputs[j], 1)
            else:
                self.pretraining(inputs[j], 0)

class sNAND(Sigmoid):

    def __init__(self):
        super().__init__([2.0, 2.0], 3)
        self.nandTraining()

    def nandTraining(self, trainInputs=100):
        inputs = []
        for i in range(trainInputs):
            par = [randint(0, 1), randint(0, 1)]
            inputs.append(par)
        for j in range(len(inputs)):
            if pNAND().feed(inputs[j]):
                self.pretraining(inputs[j], 1)
            else:
                self.pretraining(inputs[j], 0)