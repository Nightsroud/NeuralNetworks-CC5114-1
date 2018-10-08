from Percept.Perceptrons import Perceptron
from math import *

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

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        r = 0
        for x in range(len(inputs)):
            r += self.weight[x] * inputs[x]
        r += self.bias
        r2 = 1 / (1 + exp(- r))
        return r2 > 0

class sOR(Sigmoid):

    def __init__(self):
        super().__init__([1.0, 1.0], -0.5)

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        r = 0
        for x in range(len(inputs)):
            r += self.weight[x] * inputs[x]
        r += self.bias
        r2 = 1 / (1 + exp(- r))
        return r2 > 0

class sNAND(Sigmoid):

    def __init__(self):
        super().__init__([2.0, 2.0], 3)

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        r = 0
        for x in range(len(inputs)):
            r += self.weight[x] * inputs[x]
        r += self.bias
        r2 = 1 / (1 + exp(- r))
        return r2 > 0