class MyQueue:
    def __init__(self,capacity):
        self.queue = [0]*capacity
        self.front =0
        self.rear =0
        self.capacity =capacity
    def enqueue(self,element):
        if self.isFull()==True:
            print('overflow')
            return
        self.queue[self.rear]=element
        self.rear += 1
        print(f"{element} added successfully")
    def dequeue(self):
        if self.isEmpty()==True:
            print('underflow')
            return -1

        element = self.queue[self.front]
        self.front += 1
        print('removed element',element)
    def peek(self):
        if self.isEmpty()==True:
            print('underflow')
            return -1
        element = self.queue[self.front]
        print('front element',element)
    def isFull(self):
        if self.rear == self.capacity:
            return  True
        else:
            return False
    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False
    def display(self):
        return self.queue
q = MyQueue(9)
q.enqueue(89)
q.enqueue(879)
q.enqueue(896)
q.dequeue()
q.peek()
print(q.isEmpty())
print(q.display())