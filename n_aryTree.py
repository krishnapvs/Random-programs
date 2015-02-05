import Queue
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


n=Node(1)
n.add_child(Node(2))
n.add_child(Node(3))
n.add_child(Node(4))
n.children[0].add_child(Node(5))
n.children[0].add_child(Node(6))
n.children[0].add_child(Node(7))
n.children[2].add_child(Node(8))
n.children[2].add_child(Node(9))
n.children[2].add_child(Node(10))
Array=[]
Q=Queue.Queue()
Q.put(n)
Array.append(n.data)
while (not Q.empty()):
    k=Q.get()
    for i in k.children:
        Q.put(i)
        Array.append(i.data)

print Array
        
