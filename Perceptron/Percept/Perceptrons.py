class Perceptron(object):
    def __init__(self, weights, bias):
        self.weight = weights
        self.bias = bias

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        r = 0
        for x in range(len(inputs)):
            r += self.weight[x]*inputs[x]
        r+= self.bias
        return r > 0

class pAND(Perceptron):

    def __init__(self):
        Perceptron.__init__(self, [1.0, 1.0], -1.5)

class pOR(Perceptron):

    def __init__(self):
        Perceptron.__init__(self, [1.0, 1.0], -0.5)

class pNAND(Perceptron):

    def __init__(self):
        Perceptron.__init__(self, [2.0, 2.0], 3)

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