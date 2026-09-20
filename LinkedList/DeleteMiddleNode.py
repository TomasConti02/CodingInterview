class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    def append(self, data):
        anchor=self
        x=Node(data)
        
        while anchor.next is not None:
            anchor=anchor.next #go forward
        
        anchor.next=x
    def print(self):
        anchor=self

        while anchor is not None:
            print(anchor.data, end=" -> " if anchor.next else "\n")
            anchor=anchor.next 
    def DeleteMiddleNode(self):

        before=None
        anchor1=self
        anchor2=self

        while anchor2.next is not None: #O(N) in complexity

            before=anchor1 #track the precessor
            anchor1=anchor1.next
            anchor2=anchor2.next

            if anchor2.next is not None:
                anchor2=anchor2.next
        if before is None:
            print("single element list")
        else:
            before.next=anchor1.next
            
        

if __name__=="__main__":
    x=Node("a")
    x.print()
    x.append("b")
    x.append("c")
    x.append("e")
    x.append("f")
    x.append("g")
    x.print()
    x.DeleteMiddleNode()
    x.print()