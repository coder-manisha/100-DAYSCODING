class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow - the queue is empty")
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=' <- ')
            current = current.next
        print("None")


queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)

print("Queue after enqueuing 100, 200, 300:")
queue.display()

print("Dequeued item:", queue.dequeue())
print("Front item after dequeue:", queue.peek())
