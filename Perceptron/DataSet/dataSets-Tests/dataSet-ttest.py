from Network.NeuralNetwork import *
from Network.NeuralLayer import *
from Network.Neuron import *

import unittest



class NetworkTests(unittest.TestCase):


    def setUp(self):

        self.red = NeuralNetwork(2, [1, 1])
        self.layer = NeuralLayer(2, 1)
        self.layer2 = NeuralLayer(1, 1)
        self.neuron = Neuron(2)
        self.neuron2 = Neuron(1)

# testcase entregado en ucursos

    def testCase1(self):
        self.neuron.custom([0.4, 0.3], 0.5)

        self.neuron2.custom([0.3], 0.4)

        self.layer.custom([self.neuron])

        self.layer2.custom([self.neuron2])

        self.red.custom([self.layer, self.layer2])

        self.red.train([1, 1], [1])

        self.assertEqual(round(self.neuron.weight[0], 15), 0.402101508999489)

        self.assertEqual(round(self.neuron.weight[1], 15), 0.302101508999489)

        self.assertEqual(round(self.neuron2.weight[0], 15), 0.330262548639919)

        #self.assertEqual(round(self.neuron.bias, 15), 0.502101508999489)

        #self.assertEqual(round(self.neuron.bias, 15), 0.43937745312797394)



if __name__ == '__main__':
    unittest.main()
