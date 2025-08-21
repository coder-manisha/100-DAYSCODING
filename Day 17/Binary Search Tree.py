class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None
    def insertNode(self,node,val):
        n = Node(val)
        if self.root == None:
            self.root = n
            print('root node is added',val)
            return
        if val<node.val:
            if node.left == None:
                node.left = n
                print("node is added to left side")
            else:
                self.insertNode(node.left,val)
        else:
            if node.right == None:
                node.right = n
                print("node is added to right side")
            else:
                self.insertNode(node.right,val)
b = BSTree()
b.insertNode(Node,10)
b.insertNode(b.root,132)
b.insertNode(b.root,113)
b.insertNode(b.root,133)