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
        time=Node(data)
        while anchor.next is not None:
            anchor=anchor.next
        anchor.next=time
"""
    def reverse1(self):
        return self.reverse(self)

    def reverse(self, node):

        if node is None: #base case 
            return None
        
        self.reverse(node.next)
        print(node.data)
        return node.data
    
"""
def sum(node1, node2)->Node:

    anchor1=node1
    anchor2=node2
    report=0

    time=Node(-1)
    time2=time

    while anchor1 is not None or anchor2 is not None:

        if anchor1 is not None and anchor2 is not None:

            sum= (anchor1.data+anchor2.data+report)%10 #7+5=12 -> 12%10=2
            report=(anchor1.data+anchor2.data+report)//10 #7+5=12 -> 12//10=1
    
            x=Node(sum)
            time.next=x
            time=time.next

            anchor1=anchor1.next
            anchor2=anchor2.next
            continue


        if anchor1 is not None:

            sum= (anchor1.data+report)%10
            report=(anchor1.data+report)//10

            x=Node(sum)
            time.next=x
            time=time.next

            anchor1=anchor1.next
            continue

        if anchor2 is not None:
            sum= (anchor2.data+report)%10
            report=(anchor2.data+report)//10

            x=Node(sum)
            time.next=x
            time=time.next
            
            anchor2=anchor2.next
            
            continue

    return time2.next
# (7 -> 1 )        17
# (5 -> 9 -> 2)    295

if __name__=="__main__":

    x1=Node(7)
    x1.append(1)
    #x1.append(6)
    x1.print()

    x2=Node(5)
    x2.append(9)
    x2.append(2)
    x2.print()

    head=sum(x1, x2)
    head.print()
