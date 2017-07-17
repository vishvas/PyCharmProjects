import ctypes

class DynamicArray(object):
    """
    Implemented Own Dynamic Array
    """
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0<=item<=self.n:
            return IndexError("Index Out of Bound")
        return self.A[item]



    def append(self,item):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = item
        self.n +=1

    def _resize(self,capacity):
        B = self.make_array(capacity)
        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = capacity

    def __str__(self):

        string = '['
        for i in range(self.n):
             string += str(self.A[i]) + ','
        string = string[:-1] + ']'
        return string

    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()