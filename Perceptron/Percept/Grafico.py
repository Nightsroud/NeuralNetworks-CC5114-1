from Percept.Perceptrons import *
from random import *
import matplotlib.pyplot as plt

class Traning:

    def __init__(self, perceptron, trainInputs):
        self.perceptron = perceptron
        self.trainInputs = trainInputs
        self.iterTraining(self.perceptron, self.trainInputs)

    # dar desired output como una lista de valores junto con la lista de inputs a entrenar.
    def iterTraining(self, perceptron, trainInputs):
        for i in range(len(trainInputs)):
            if 2*trainInputs[i][0] + 5 < trainInputs[i][1]:
                perceptron.pretraining(trainInputs[i], 1)
            else:
                perceptron.pretraining(trainInputs[i], 0)
        return perceptron


class Graficar:
    # @Param Iter: Numero de iteraciones para el entrenamiento
    # @Param Pnts: Numero de puntos a graficar
    # Constructor de clase Graficar
    def __init__(self, Iter, cantPuntos):
        self.perceptron = Perceptron([uniform(-2, 2), uniform(-2, 2)], uniform(-2, 2))
        self.train = Traning(self.perceptron, self.generarInputs(Iter))
        self.perceptPlot(self.generarInputs(cantPuntos))

    # @Param N: Numero de pares de inputs
    # Funcion auxiliar que genera un numero N de pares de inputs
    def generarInputs(self, Iter):
        inputs = []
        for i in range(Iter):
            par = [uniform(0,100), uniform(0,100)]
            inputs.append(par)
        return inputs

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


class Curva:

    def __init__(self, cantidadInputs, numeroEntrenamientos, perceptron, numeroIteraciones):
        self.perceptron = perceptron
        self.learningCurve(perceptron, cantidadInputs, numeroEntrenamientos, numeroIteraciones)

    def learningCurve(self, percept, cI, nE, nI):
        iterInputs = []
        for x in range(cI):
            iterInputs.append(self.generarInput())
        aciertosT = []
        aciertos = 0
        for i in range(nI):
            for j in range(len(iterInputs)):
                aciertos += (self.sobreCurva(iterInputs[j][0], iterInputs[j][1]) == percept.feed(iterInputs[j]))
            aciertosT.append(aciertos/cI)
            aciertos = 0
            testInputs = []
            for k in range(nE):
                testInputs.append(self.generarInput())
            self.perceptronTraining(percept, testInputs)
        plt.plot(range(nI), aciertosT, '-')
        plt.show()

    def generarInput(self):
        return [uniform(0, 100), uniform(0, 100)]

    def sobreCurva(self, x, y):
        if 2*x + 5 < y:
            return True
        else:
            return False

    def perceptronTraining(self, perceptron, inputs):
        for i in range(len(inputs)):
            if 2*inputs[i][0] + 5 < inputs[i][1]:
                perceptron.pretraining(inputs[i], 1)
            else:
                perceptron.pretraining(inputs[i], 0)

    # Falta curva de tendencias, hits vs miss, cuantos puntos fueron graficados bien de acuerdo a la cantidad de entrenamiento.
Graficar(10000, 100)
# Curva(200, 100, Perceptron([uniform(-2, 2), uniform(-2, 2)], uniform(-2, 2)), 20)