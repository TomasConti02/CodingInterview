class Stack: # stack implementation of the stack by linked list, very easy but data in memory are not locally (many cache miss)
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None  

    def push(self, data): #O(1)

        x = self.Node(data)
        x.next = self.top  #2. Il nuovo nodo 'x' punta a quello che *fino a un momento fa* era il top
        self.top = x # 3. Sposti il puntatore 'top' sul nuovo nodo 'x'
    """
    top ➔ None

    stack.push(1)
    top ➔ [ 1 | next=None ]

    stack.push(2)
    top ➔ [ 2 | next ] ➔ [ 1 | next=None ].

    """
    def pop(self): #O(1)
        if self.top is None:
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self): #O(1)
        if self.top is None:
            return None
        return self.top.data

    def isEmpty(self):
        return self.top is None

    # --- NUOVO METODO DI PRINT ---
    def display(self):
        if self.isEmpty():
            print("Lo stack è vuoto.")
            return
        
        current = self.top
        print("--- TOP ---")
        while current is not None:
            print(f"|  {current.data}  |")
            current = current.next
        print("-----------")

class StackByArray: 
    
    def __init__(self):
        self.array=[]
    def push(self, data):
        self.array.append(data)
    def pop(self):
        self.array.pop() #remove the first element if not specify
        #last element -> pop complexity of O(1)
        #first element -> pop complexity of O(N) because the shift needed
    def print(self):
        print(self.array)

class MultiStackByDict: 

    def __init__(self):
        # Usiamo un dizionario invece di una lista
        self.stacks = {}

    def push(self, data, index):
        # Se l'indice non esiste ancora nel dizionario, creiamo una lista vuota
        if index not in self.stacks:
            self.stacks[index] = []
        
        self.stacks[index].append(data)

    def pop(self, index):
        # Controlliamo se lo stack esiste ed è popolato
        if index not in self.stacks or not self.stacks[index]:
            print(f"Errore: Lo stack {index} è vuoto!")
            return None
        
        # Rimuove e restituisce l'ultimo elemento dello stack specifico
        return self.stacks[index].pop()

    def print(self):
        if not self.stacks:
            print("Nessuno stack presente.")
            return
        
        for index, stack in self.stacks.items():
            print(f"Stack {index}: {stack}")



if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stato dello stack dopo i push:")
    stack.display()
    
    print("\nFaccio un pop:", stack.pop())
    
    print("\nStato dello stack dopo il pop:")
    stack.display()

    print("\nFaccio un pop:", stack.pop())

    print("\nStato dello stack dopo il pop:")
    stack.display()

    stack.push(2)
    stack.display()
    print("\n ################################################ ")
    time=StackByArray()
    time.push(1)
    time.push(2)
    time.push(3)
    time.print()
    time.pop()
    time.print()
    time.pop()
    time.print()
    ms = MultiStackByDict()
    ms.push("A", 0)
    ms.push("B", 0)
    ms.push("X", 5) # Possiamo usare qualsiasi indice, anche non consecutivo!
    
    print("Stato iniziale:")
    ms.print()
    
    print("\nEseguo pop dallo stack 0:", ms.pop(0))
    
    print("\nStato finale:")
    ms.print()