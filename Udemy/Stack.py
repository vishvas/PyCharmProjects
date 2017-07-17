class Stack(object):
    size = 0
    def __init__(self):
        self.list =[]

    def push(self,element):
        self.list.append(element)
        Stack.size +=1

    def pop(self):
        result = self.list[Stack.size-1]
        self.list = self.list[:-1]
        Stack.size -= 1
        return result

    def get_size(self):
        return Stack.size

    def is_empty(self):
        if Stack.size > 0:
            return False
        else:
            return True
    def peek(self):
        if Stack.size > 0:
            return self.list[Stack.size-1]
        else:
            return None



    def __str__(self):
        return ','.join(str(x) for x in self.list)