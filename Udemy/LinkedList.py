

class Node(object):
    def __init__(self,element):
        self.element = element
        self.next= None


    def get_next(self):
        return self.next

    def get_item(self):
        return self.element


class LinkedList(object):
    head = None
    size = 0


    def __init__(self):
        LinkedList.head = None
        LinkedList.size = 0



    def add(self, other):
        if LinkedList.head == None:
            LinkedList.head = Node(other)
        else:
            temp = LinkedList.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(other)


    def search(self,other):
        temp = LinkedList.head
        if temp !=None:
            while temp.next !=None:
                if temp.element == other:
                    return temp
                else:
                    temp = temp.next
            if temp.element == other:
                return temp
        return None

    def remove(self,other):
        temp = LinkedList.head
        previous = None
        if temp != None:
            if temp.element == other:
                LinkedList.head = temp.next
                del(temp)
            else:
                while temp.next !=None:
                    if temp.element == other:
                        previous.next = temp.next
                        return None
                    else:
                        previous = temp
                        temp = temp.next
                if temp.element==other:
                    previous.next = None
                    del(temp)
                    return None
        else:
            return None



    def __str__(self):
        s = ""
        p = LinkedList.head
        if p != None:
            while p.next != None:
                s += p.element
                p = p.next
            s += p.element
        return s

