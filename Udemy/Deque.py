class Deque(object):
    size = 0

    def __init__(self):
        self.list = []

    def add_rear(self, element):
        self.list.append(element)
        Deque.size += 1

    def add_front(self, element):
        self.list.insert(0,element)
        Deque.size +=1

    def remove_rear(self):
        result = self.list[Deque.size - 1]
        self.list = self.list[:-1]
        Deque.size -= 1
        return result

    def remove_front(self):
        result = self.list[0]
        self.list = self.list[1:]
        Deque.size -= 1
        return result

    def get_size(self):
        return Deque.size

    def isEmpty(self):
        if Deque.size > 0:
            return False
        else:
            return True

    def __str__(self):
        return ','.join(map(str, self.list[::-1]))