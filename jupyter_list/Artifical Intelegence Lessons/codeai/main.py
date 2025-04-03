import numpy as np


class Neuron:
    def __init__(self,w):
        self.w = w
    def y(self,x):
        s = np.dot(self.w,x)
        return s
    


inp = np.array([2,3])
wei = np.array([1,1])


neu = Neuron(wei)

print(neu.y(inp))




# https://youtu.be/TJGH_5VMAL4