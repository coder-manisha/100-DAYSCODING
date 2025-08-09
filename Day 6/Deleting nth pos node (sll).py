class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Single:
    def __init__(self):
        self.root = None

    def inseratbeg(self, val):
        n = Node(val)
        n.next = self.root
        self.root = n
        print("added", val)

    def insert_at_position(self, pos, val):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.root
            self.root = new_node
            print("Inserted", val, "at position", pos)
            return

        temp = self.root
        count = 0

        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            print("Position out of bounds.")
            return

        new_node.next = temp.next
        temp.next = new_node
        print("Inserted", val, "at position", pos)

    def delete_at_position(self, pos):
        if self.root is None:
            print("List is empty.")
            return

        if pos == 0:
            print("Deleted", self.root.val, "from position", pos)
            self.root = self.root.next
            return

        temp = self.root
        count = 0

        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            print("Position out of bounds.")
            return

        print("Deleted", temp.next.val, "from position", pos)
        temp.next = temp.next.next

    def display(self):
        temp = self.root
        while temp:
            print(temp.val, end=' -> ')
            temp = temp.next
        print("None")
s = Single()
s.inseratbeg(67)
s.inseratbeg(675)
s.inseratbeg(676)
s.insert_at_position(1, 999)
s.display()
s.delete_at_position(2)  # Deletes 675
s.delete_at_position(0)  # Deletes 676 (head)
s.delete_at_position(10) # Invalid
s.display()
