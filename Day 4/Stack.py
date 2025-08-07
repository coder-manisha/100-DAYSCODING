class MyStack:
    def __init__(self,capacity):
        self.stack = [0]*capacity
        self.top =-1
        self.capacity = capacity
    def push(self,element):
        if self.top == self.capacity-1:
            print('stack overflow')
            return
        self.top +=1
        self.stack[self.top]=element
        print('element added successfully ',element)
    def pop(self):
        if self.isEmpty()==True:
            print("stack underlflow")
            return -1
        self.top-=1
        element = self.stack[self.top]
        print('top element is  : ', element)
    def peek(self):
        if self.isEmpty()==True:
            print("stack underlflow")
            return -1
        element = self.stack[self.top]
        print('element removed : ', element)
    def isFull(self):
        return self.top == self.capacity-1
    def isEmpty(self):
        return self.top==-1
    def display(self):
        for i in range(self.top,-1,-1):
            print(f'present elements are {self.stack[i]}')
s = MyStack(10)
s.push(99)
s.push(10)
s.push(101)
s.peek()
s.pop()
s.display()