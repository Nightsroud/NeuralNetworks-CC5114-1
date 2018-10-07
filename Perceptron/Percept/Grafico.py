from Percept.Perceptrons import *
from random import *
import matplotlib.pyplot as plt


class Graficar:

    def __init__(self, N):
        self.coords = []
        self.perceptron = Perceptron([uniform(-2, 2), uniform(-2, 2)], uniform(-2, 2))
        self.generarInputs(N)

    def generarInputs(self, N):
        self.inputs = []
        for i in range(N):
            par = [uniform(0,100), uniform(0,100)]
            self.inputs.append(par)
        self.perceptronTraining(self.inputs)

    def perceptronTraining(self, inputs):
        for i in range(len(inputs)):
            if (7*i + 5) < inputs[i][1]:
                self.perceptron.pretraining(inputs[i], 1)
            else:
                self.perceptron.pretraining(inputs[i], 0)

        self.perceptPlot(inputs)

    def perceptPlot(self, inputs):
        y =[]
        for i in range(100):
            y.append(7*i + 5)
        plt.plot(range(100), y, 'g')
        for j in range(len(inputs)):
            if self.perceptron.feed(inputs[j]):
                plt.plot(inputs[j][0], inputs[j][1], 'bo')
            else:
                plt.plot(inputs[j][0], inputs[j][1], 'ro')

