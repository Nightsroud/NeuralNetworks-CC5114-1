from Network.Neuron import Neuron


class NeuralLayer:

    def __init__(self, nInputs , nNeurons):
        self.neurons = []
        self.outputs = []
        for i in range(nNeurons):
            neur = Neuron(nInputs)
            self.neurons.append(neur)



    def feed(self, someInputVariables):
        for i in range(len(self.neurons)):
            self.neurons[i].feed(someInputVariables)
        outs = []
        for j in range(len(self.neurons)):
            outs.append(self.neurons[j].getOutput())
        self.outputs = outs
        return self.outputs

    def getOutputs(self):
        return self.outputs

    def setUpLastLayer(self, expOut):
        for i in range(len(self.neurons)):
            self.neurons[i].calcLastLayerError(expOut[i])
            self.neurons[i].calcDelta(self.outputs[i])

    def setUpLayer(self, nextLayer):
        error = 0
        for i in range(len(self.neurons)):
            for j in range(len(nextLayer.getNeurons())):
                error += nextLayer.getNeurons()[j].getWeights()[i] * nextLayer.getNeurons()[j].getDelta()
            self.neurons[i].calcDeltaExtError(error)
            error = 0

    def resetNeuronErrors(self):
        for i in range(len(self.neurons)):
            self.neurons[i].resetError()

    def getNeurons(self):
        return self.neurons

    def layerTraining(self):
        for i in range(len(self.neurons)):
            self.neurons[i].update()
