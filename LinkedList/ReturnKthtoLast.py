class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def append(self, data):
        time=Node(data) #creation of a node alone
        anchor=self #start the anchor pointer to the head (the first node) the one of the istance
        while anchor.next is not None:
            anchor=anchor.next
        anchor.next=time

    def print(self):
        anchor=self
        while anchor is not None:
            print(anchor.data, end=" -> " if anchor.next else "\n")
            anchor=anchor.next
    def ReturnKthtoLast(self, kth): #probablity by a stack or queue
        stack = []

        anchor=self
        while anchor is not None:
            stack.append(anchor.data)
            anchor=anchor.next
        #return stack[-kth:]
        result = [stack.pop() for _ in range(kth)]
        #reverse work in place and return a None and change the list in place 
        result.reverse()
        return result

if __name__=="__main__":
    x=Node(20)
    x.append(1)
    x.append(3)
    x.append(4)
    x.append(3)
    x.append(3)
    x.print()
    print(x.ReturnKthtoLast(3))