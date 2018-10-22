from Network.NeuralLayer import NeuralLayer

class NeuralNetwork:

    def __init__(self, nInputs, nNeurCapas):
        self.Layers = []
        self.output = 0
        self.delta = 0
        Inputs = nInputs
        for i in range(len(nNeurCapas)):
            layer = NeuralLayer(Inputs, nNeurCapas[i])
            self.Layers.append(layer)
            Inputs = nNeurCapas[i]

    def feed(self, someInputValues):
        # Primera iteracion son los inputs iniciales para la primera capa
        InFromOuts = someInputValues
        # For para iterar sobre todas las capas, hasta llegar a la ultima
        for i in range(len(self.Layers)):
            # Itera en el layer con los inputs dados
            self.Layers[i].feed(InFromOuts)
            # Convierto los inputs de la siguiente iteracion en los outputs de la iteracion anterior
            InFromOuts = self.Layers[i].getOutputs()
        # Al finalizar las iteraciones el output de la red es el output que arrojo el ultimo layer
        self.output = InFromOuts


    # errors = newArrayList();
    # Error = sum(abs(expectedOutput - realOutput)^2)
    # sum un numero n de ejemplos dados a la red y errors.add(error)
    def train(self, trainingInputs, expOut):
        self.feed(trainingInputs)
        actualLayer = len(self.Layers) - 1
        nextLayer = 0
        while actualLayer >= 0:
            if actualLayer == len(self.Layers) - 1:
                self.Layers[actualLayer].setUpLastLayer(expOut)
                self.Layers[actualLayer].resetNeuronErrors()
                nextLayer = actualLayer
                actualLayer -= 1
            else:
                self.Layers[actualLayer].setUpLayer(self.Layers[nextLayer])
                nextLayer = actualLayer
                actualLayer -= 1
        for i in range(len(self.Layers)):
            self.Layers[i].layerTraining()

    def realTraining(self, trainingInputs, expOut):
        for i in range(len(trainingInputs)):
            self.train(trainingInputs[i], expOut[i])


    def getOutput(self):
        return self.output