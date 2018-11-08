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

        self.red2 = NeuralNetwork(2, [2, 2])

        self.lay1 = NeuralLayer(2, 2)

        self.lay2 = NeuralLayer(2, 2)

        self.neur1 = Neuron(2)

        self.neur2 = Neuron(2)

        self.neur3 = Neuron(2)

        self.neur4 = Neuron(2)

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

        self.assertEqual(round(self.neuron.bias, 15), 0.502101508999489)

        self.assertEqual(round(self.neuron2.bias, 15), 0.439377453127974)

    def testCase2(self):
        self.neur1.custom([0.7, 0.3], 0.5)

        self.neur2.custom([0.3, 0.7], 0.4)

        self.neur3.custom([0.2, 0.3], 0.3)

        self.neur4.custom([0.4, 0.2], 0.6)

        self.lay1.custom([self.neur1, self.neur2])

        self.lay2.custom([self.neur3, self.neur4])

        self.red2.custom([self.lay1, self.lay2])

        self.red2.train([1, 1], [1, 1])

        self.assertEqual(round(self.neur1.weight[0], 15), 0.702510448549328)

        self.assertEqual(round(self.neur1.weight[1], 15), 0.302510448549328)

        self.assertEqual(round(self.neur2.weight[0], 15), 0.302498011357483)

        self.assertEqual(round(self.neur2.weight[1], 15), 0.702498011357483)

        self.assertEqual(round(self.neur3.weight[0], 15), 0.229947378819557)

        self.assertEqual(round(self.neur3.weight[1], 15), 0.329383628639501)

        self.assertEqual(round(self.neur4.weight[0], 15), 0.419430056526462)

        self.assertEqual(round(self.neur4.weight[1], 15), 0.219064291698386)

        self.assertEqual(round(self.neur1.bias, 15), 0.502510448549328)

        self.assertEqual(round(self.neur2.bias, 15), 0.402498011357483)

        self.assertEqual(round(self.neur3.bias, 15), 0.336629542251590)

        self.assertEqual(round(self.neur4.bias, 15), 0.623765488150905)


if __name__ == '__main__':
    unittest.main()
