class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.root = None
        self.tail = None
    def addNode(self,val):
        n = Node(val)
        if self.root == None:
            self.root = n
            self.tail = n
            return
        self.tail.next = n
        n.prev = self.tail
        self.tail= n
        temp = self.root
    def display(self):
        temp = self.root
        while temp:
            print(temp.val,end =' -> ')
            temp = temp.next
d = DoubleLinkedList()
d.addNode(12)
d.addNode(124)
d.display()