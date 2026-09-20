class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def print(self):
        anchor=self

        while anchor is not None:
            print(anchor.data, end=" -> " if anchor.next else "\n")
            anchor=anchor.next

    def append(self, data):
        anchor=self

        while anchor.next is not None:
            anchor=anchor.next

        anchor.next=Node(data)

    def append_node(self, node):
        anchor=self

        while anchor.next is not None:
            anchor=anchor.next

        anchor.next=node

def intersection(node1:Node, node2:Node):    

    anchor1=node1
    anchor2=node2

    time=set()#O(N)

    while anchor1 is not None: #O(N)
        time.add(anchor1) #O(N)
        anchor1=anchor1.next

    while anchor2 is not None: #O(N)
        if anchor2 in time: #O(1)
            return True
        anchor2=anchor2.next

    return False
if __name__=="__main__":

    shared=Node(100000)

    x=Node(1)
    x.append(2)
    x.append(3)
   # x.append_node(shared)
    x.append(4)
    x.append(5)

    y=Node(1)
    y.append(2)
    y.append(3)
    y.append(4)
    y.append_node(shared)
    y.append(5)

    x.print()
    y.print()

    print(intersection(x, y))