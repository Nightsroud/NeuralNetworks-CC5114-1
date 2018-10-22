import random

class Perceptron(object):

    # Constructor del perceptron
    def __init__(self, weights, bias):
        self.weight = weights
        self.bias = bias

    # Alimenta al perceptron una catnidad de inputs iguales a su peso
    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        r = 0
        for x in range(len(inputs)):
            r += self.weight[x]*inputs[x]
        r+= self.bias
        return r > 0

    # Entrena el preceptron (1 iteracion)
    def pretraining(self, inputs, desiredOutput):
        realOutput = self.feed(inputs)
        diff = desiredOutput - realOutput
        lr = 0.1
        for N in range(len(inputs)):
            self.weight[N] += (lr*float(inputs[N])*diff)
        self.bias += (lr*diff)



class pAND(Perceptron):

    def __init__(self):
        super().__init__([1.0, 1.0], -1.5)

class pOR(Perceptron):

    def __init__(self):
        super().__init__([1.0, 1.0], -0.5)

class pNAND(Perceptron):

    def __init__(self):
        super().__init__([-2.0, -2.0], 3)

class pSum(object):
    sNAND = pNAND
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def feed(self):
        result1 = self.sNAND.feed([self.x1, self.x2])
        carry = self.sNAND.feed(result1, result1)
        result2 = self.sNAND.feed([self.x1, result1])
        result3 = self.sNAND.feed([result1, self.x2])
        result = self.sNAND.feed([result2, result3])
        return (result, carry)



#tAnd = pAND()
#print(tAnd.feed([1.0, 1.0, 1.0]))