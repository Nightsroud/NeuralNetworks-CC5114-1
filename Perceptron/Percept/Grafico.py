from Percept.Perceptrons import *
from random import *
import matplotlib.pyplot as plt


class Graficar:
    # @Param Iter: Numero de iteraciones para el entrenamiento
    # @Param Pnts: Numero de puntos a graficar
    # Constructor de clase Graficar
    def __init__(self, Iter, Pnts):
        self.perceptron = Perceptron([uniform(-2, 2), uniform(-2, 2)], uniform(-2, 2))
        self.perceptronTraining(self.generarInputs(Iter), Pnts)

    # @Param N: Numero de pares de inputs
    # Funcion auxiliar que genera un numero N de pares de inputs
    def generarInputs(self, N):
        inputs = []
        for i in range(N):
            par = [uniform(0,100), uniform(0,100)]
            inputs.append(par)
        return inputs

    # @Param inputs: Lista de pares de inputs
    # @Param Pnts: Cantidad de puntos a plotear
    # Entrenamiento del perceptron con la lista de pares de inputs.
    def perceptronTraining(self, inputs, Pnts):
        for i in range(len(inputs)):
            if (2*inputs[i][0] + 5) < inputs[i][1]:
                self.perceptron.pretraining(inputs[i], 1)
            else:
                self.perceptron.pretraining(inputs[i], 0)

        self.perceptPlot(self.generarInputs(Pnts))

    # @Param inputs: Lista de pares de inputs a graficar
    # Genera un grafico con los puntos de la lista de acuerdo al entrenamiento del perceptron.
    def perceptPlot(self, inputs):
        y =[]
        for i in range(100):
            y.append(2*i + 5)
        plt.plot(range(100), y, 'g')
        for j in range(len(inputs)):
            if self.perceptron.feed(inputs[j]):
                plt.plot(inputs[j][0], inputs[j][1], 'bo')
            else:
                plt.plot(inputs[j][0], inputs[j][1], 'ro')
        plt.show()

# Graficar(10000, 100)