class Node:
    #self is the object instace injected be the rutime
    def __init__(self, data): # Each node stores data and a reference to the next node
        self.data = data
        self.next = None

    def appendToTail(self, data): #at each operation restart always on the start head
        # Create a new node to be added at the end
        tail = Node(data) #the reference to the next node of this node is None
        # Start from the current node
        n = self # take the node istance
        while n.next is not None: # Traverse the list until we reach the last node (where next is None)
            n = n.next
        # Link the last node to the new node
        n.next = tail

    def print_list(self):
        n = self
        while n is not None:
            print(n.data, end=" -> " if n.next else "\n")
            n = n.next

    def RemoveDups(self): #if we want execute this operation in place ?
        dups=set()

        n=self
        before=self

        if n is None:
            return
         
        while n is not None: #O(N) in runtime complexity and O(N) in space complexity
            
            if n.data in dups:
                before.next=n.next #execute only the forward skip
                
            else:
                dups.add(n.data)
                before=n # move on the pointer

            n=n.next #alaways move one

if __name__ == "__main__":
    # Create the first node (head of the list)
    x = Node(1)

    # Append elements to the end of the list
    x.appendToTail(2)

    x.appendToTail(3)
    x.appendToTail(3)
    x.appendToTail(3)

    x.appendToTail(4)
    x.appendToTail(4)
    x.appendToTail(5)
    x.appendToTail(4)
    x.appendToTail(6)
    #    1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 4
    """
    (1)
    (1, 2)
    (1, 2, 3)

    (1, 2, 3)  |||||||||| 1 -> 2 -> 3  -> 3 -> 4 -> 4
    (1, 2, 3)  |||||||||| 1 -> 2 -> 3  -> 4 -> 4
    (1, 2, 3, 4)
    (1, 2, 3, 4)
    (1, 2, 3, 4, 5)
    (1, 2, 3, 4, 5)
    (1, 2, 3, 4, 5, 6)
    """
    # Print the full linked list
    x.print_list()
    x.RemoveDups()
    x.print_list()