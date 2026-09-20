class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            
    def __init__(self):
        self.top = None 
        self.min_stack = [] #min stack 
        # the smallest item is in the array last poinzione tail [-1]
    def push(self, data):
        #added items only if are smaller, smallest is in the tail 
        if not self.min_stack or data <= self.min_stack[-1]: #-1 is the stack top
            self.min_stack.append(data) #O(1)
            
        time = self.Node(data)
        time.next = self.top
        self.top = time

    def pop(self):
        if self.top is None:
            return None

        output = self.top.data
        self.top = self.top.next
        # it is the most important control 
        # removed the tail only if i am removing this values
        # it is no possible remove other value before the tail because the stack behaviour
        if output == self.min_stack[-1]: #min stack pop of the tail only if it waas the removed
            self.min_stack.pop() #O(1)
            
        return output

    def get_min(self): 
        if not self.min_stack:
            return None
        return self.min_stack[-1] #tail item is the smallest 
    
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


# =====================================================================
# TESTING COMPLETO
# =====================================================================
if __name__ == "__main__":
    x = Stack()
    
    print("=== TEST 1: Operazioni su Stack Vuoto ===")
    print("peek():", x.peek())          # Deve stampare None
    print("pop():", x.pop())            # Deve stampare None
    print("get_min():", x.get_min())    # Deve stampare None
    print("isEmpty():", x.isEmpty())    # Deve stampare True
    x.display()                         # Deve stampare [ Stack Vuoto ]
    print("-" * 40)

    print("\n=== TEST 2: Inserimenti in ordine sparso ===")
    x.push(4)
    x.push(7)
    x.push(2)
    x.push(9)
    x.display()
    print("Minimo attuale (atteso 2):", x.get_min())
    print("In cima allo stack (atteso 9):", x.peek())
    print("-" * 40)

    print("\n=== TEST 3: Rimozione del non-minimo ===")
    print("Pop effettuato:", x.pop()) # Rimuove 9
    print("Minimo attuale dopo pop (atteso ancora 2):", x.get_min())
    print("-" * 40)

    print("\n=== TEST 4: Rimozione del minimo attuale ===")
    print("Pop effettuato:", x.pop()) # Rimuove 2
    print("Minimo attuale dopo pop (atteso 4):", x.get_min())
    x.display()
    print("-" * 40)

    print("\n=== TEST 5: Il caso limite dei duplicati (Molto Importante!) ===")
    # Se inseriamo due minimi uguali, il sistema deve tracciarli entrambi
    x.push(3)
    x.push(3) # Duplicato del minimo
    x.display()
    print("Minimo attuale (atteso 3):", x.get_min())
    
    print("\nRimuovo il primo dei due '3'...")
    x.pop()
    print("Minimo attuale (deve rimanere 3):", x.get_min()) 
    
    print("\nRimuovo anche il secondo '3'...")
    x.pop()
    print("Minimo attuale (deve tornare a 4):", x.get_min())
    print("-" * 40)

    print("\n=== TEST 6: Svuotamento totale e ripristino ===")
    print("Rimuovo l'ultimo elemento rimasto (4):", x.pop())
    print("Lo stack è vuoto?", x.isEmpty()) # Deve essere True
    print("get_min() su stack svuotato:", x.get_min()) # Deve essere None
    
    print("\nReinserisco un elemento dopo lo svuotamento:")
    x.push(42)
    print("Nuovo minimo (atteso 42):", x.get_min())
    x.display()
    print("=" * 40)