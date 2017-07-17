class Queue2Stacks(object):
    def __init__(self):
        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)


    def dequeue(self):
        if len(self.stack2) >0:
            return self.stack2.pop()
        else:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
            return self.stack2.pop()

