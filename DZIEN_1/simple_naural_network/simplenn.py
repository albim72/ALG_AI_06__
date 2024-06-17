import numpy as np

class SimpleNeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1))-1 #mnożenie przez 2 poszerza zkres [0,1] dp [-1,1]
        
    def __new__(cls, *args, **kwargs):
        pass
    
