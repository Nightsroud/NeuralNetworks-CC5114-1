from Percept.Sigmoid import *
from random import *

class Neuron(object):

    def __init__(self, nInputs, lr=0.5):
        self.weight = []
        self.bias = uniform(-2, 2)
        for i in range(nInputs):
            self.weight.append(uniform(-2, 2))
        self.output = 0
        self.delta = 0
        self.error = 0
        self.lr = lr
        self.lastInput = []

    def feed(self, someInputVariables):
        assert len(someInputVariables) == len(self.weight)
        self.lastInput = someInputVariables
        r = 0
        for x in range(len(someInputVariables)):
            r += self.weight[x] * someInputVariables[x]
        r += self.bias
        r2 = 1 / (1 + exp(- r))
        self.output = r2
        return r2

    def getOutput(self):
        return self.output

    def calcLastLayerError(self, expOut):
        self.error = expOut - self.output

    def getError(self):
        return self.error

    def setError(self, extError):
        self.error = extError

    def resetError(self):
        self.error = 0

    def transferDerivate(self, output):
        return output*(1 - output)

    def calcDelta(self, output):
        self.delta = self.error * self.transferDerivate(output)

    def calcDeltaExtError(self, error):
        self.delta = error * self.transferDerivate(self.getOutput())

    def getDelta(self):
        return self.delta

    def getWeights(self):
        return self.weight

    def getLr(self):
        return self.lr

    def getLastInputs(self):
        return self.lastInput

    def update(self):
        for i in range(len(self.weight)):
            self.weight[i] += self.getLr() * self.getDelta() * self.getLastInputs()[i]
        self.bias += self.getLr() * self.getDelta()

    def custom(self, weightList, bias):
        self.weight = weightList
        self.bias = bias