class Stack:

    class Node:
        def __init__(self, data):
            self.next=None
            self.data=data
            
    def __init__(self):
        self.top=None #empty stack 

    def push(self, data):
        time=self.Node(data)
        time.next=self.top
        self.top=time

    def pop(self):
        if self.top is None:
            return None
        
        data=self.top.data
        self.top=self.top.next
        return data
    def display(self):
        if self.isEmpty():
            print("[ Stack Vuoto ]")
            return
        
        current = self.top
        print("--- TOP ---")
        while current is not None:
            print(f"|  {current.data}  |")
            current = current.next
        print("-----------")

    def peek(self): 
        if self.top is None:
            return None
        return self.top.data

    def isEmpty(self):
        return self.top is None

class SetOfStacks:

    class Node:
        def __init__(self, data):
            self.next=None
            self.data=data
    class Stack:
        def __init__(self):
            self.top = None
            self.size = 0  #need to track the dimensione of the single stack

    def __init__(self,th):
        #as soon as a stack exceed the capacity th start a new stack
        self.set_of_stacks=[] #it is a list of stacks
        self.th=th
        self.num=0 #track the number of the items

    def popAt (self, index):

        if self.set_of_stacks[index].top is None:
            return None
        
        output=self.set_of_stacks[index].top.data
        self.set_of_stacks[index].top=self.set_of_stacks[index].top.next
        self.set_of_stacks[index].size-=1
        return output

    def pushAt (self, data, index):
        time=self.Node(data)

        time.next=self.set_of_stacks[index].top
        self.set_of_stacks[index].top=time
        self.set_of_stacks[index].size+=1



    def push(self, data):
        if not self.set_of_stacks or self.set_of_stacks[-1].size == self.th:
            self.set_of_stacks.append(self.Stack())

        index=len(self.set_of_stacks)-1 #indert the data int the last stack
        self.pushAt(data, index)
        self.num+=1

    def pop(self):

        if self.num==0:
            return None
        
        index=len(self.set_of_stacks) -1
        self.popAt(index)
        self.num-=1

        if self.set_of_stacks[-1].size==0:
            self.set_of_stacks.pop()
        

    def display(self):
        """Visualizza lo stato corrente di tutti gli stack nel set."""
        if not self.set_of_stacks:
            print("SetOfStacks è vuoto.")
            return

        print(f"\n--- STATO DEL SET OF STACKS (Totale elementi: {self.num}) ---")
        
        # Scorriamo gli stack al contrario (dall'ultimo creato al primo)
        # o in ordine normale. Di solito in ordine normale (0, 1, 2...) è più intuitivo.
        for index, stack in enumerate(self.set_of_stacks):
            print(f"Stack [{index}] (Size: {stack.size}/{self.th}):", end=" ")
            
            # Se lo stack è vuoto (può succedere temporaneamente dopo un popAt intermediate)
            if stack.top is None:
                print("Vuoto")
                continue
            
            # Scorriamo i nodi dello stack corrente
            current = stack.top
            elements = []
            while current:
                elements.append(str(current.data))
                current = current.next
            
            # Mostriamo gli elementi separati da frecce. 
            # Il primo elemento stampato è il TOP dello stack.
            print(" -> ".join(elements) + " -> None (Bottom)")
            
        print("-" * 50 + "\n")

if __name__=="__main__":
    x=SetOfStacks(3)

    y=Stack()
    y.push(2)
    y.push(3)
    y.push(4)
    y.display()
    y.pop()
    y.display()

    x.push(1)
    x.push(1)
    x.push(1)
    x.push(1)
    x.display()
    x.pop()
    x.pop()
    x.pop()
    x.display()
