class tree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def isLeaf(self):
        if self.left is None:
            return True
        else:
            return False

    def calculate(self):
        if self.left is None:
            return self.value
        else:
            return str(self.left.calculate())+str(self.value)+str(self.right.calculate())

    def evaluate(self):
        retval = self.calculate()
        return eval(retval)


    def setLeft(self, leftTree):
        self.left = leftTree

    def setRight(self, rightTree):
        self.right = rightTree

    def setValue(self, value):
        self.value = value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value
if __name__ == '__main__':
    f = tree(0)
    print(f.isLeaf())