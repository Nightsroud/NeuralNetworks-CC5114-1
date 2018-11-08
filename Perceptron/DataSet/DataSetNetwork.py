from Network.NeuralNetwork import *
from DataSet.trainReader import *
from DataSet.dataReader import *
from random import *
import time
import matplotlib.pyplot as plt




class dataSet:

    def __init__(self, nEpochs=500, nInputs=8, nNeurCapas=[8, 19]):
        self.red = NeuralNetwork(nInputs, nNeurCapas)
        self.lineList = trainReader()
        self.outputList = []
        shuffle(self.lineList)
        self.outlist(self.lineList, self.outputList)
        # self.datatrain(nEpochs)
        print("Funciono Entrenamiento: CheckPoint 1")
        self.dataList = dataReader()
        self.dataOut = []
        self.outlist(self.dataList, self.dataOut)
        self.curveTraining()

    def outlist(self, lineList, outList):
        for i in lineList:
            zerolist = [0]*19
            zerolist[i.pop(0)] = 1
            outList.append(zerolist)

    def datatrain(self, nEpoch):
        for j in range(nEpoch):
            #start = time.time()
            self.red.realTraining(self.lineList, self.outputList)
            #end = time.time()
            #print(end - start)

    def curveTraining(self):
        totallineas = len(self.dataList)
        contpres = 0.0
        error = 0
        xaprendizaje = []
        yaprendizaje = []
        xerror = []
        yerror = []
        for k in range(7):
            for l in range(len(self.dataList)):
                self.red.feed(self.dataList[l])
                for m in range(len(self.red.output)):
                    absdif = abs(self.dataOut[l][m] - self.red.output[m])
                    if absdif < 0.5:
                        contpres += 1
                    error+= absdif**2
                contpres /= 19
            contpres /= totallineas
            xaprendizaje.append(k)
            yaprendizaje.append(contpres)
            contpres = 0
            xerror.append(k)
            yerror.append(error)
            error = 0
            self.datatrain(k*100 + 100)
        plt.figure(1)
        plt.subplot(211)
        plt.xlabel("Numero de Epochs")
        plt.ylabel("Cura de Aprendizaje")
        plt.plot(xaprendizaje, yaprendizaje, 'b-')
        plt.subplot(212)
        plt.xlabel("Numero de Epochs")
        plt.ylabel("Error")
        plt.plot(xerror, yerror, 'r-')
        plt.show()



if __name__ == "__main__":
    dataSet()