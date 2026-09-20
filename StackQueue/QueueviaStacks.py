class MyQueue: # Queue is FIFO (First In First Out)

    class Stack:
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None
                
        def __init__(self):
            self.top = None

        def push(self, data):
            time = self.Node(data)
            time.next = self.top
            self.top = time

        def pop(self):
            if self.top is None:
                return None
            data = self.top.data
            self.top = self.top.next
            return data
        
        def peek(self):
            if self.top is None:
                return None
            return self.top.data
        
        def isEmpty(self):
            return self.top is None
            
        def display(self):
            if self.isEmpty():
                print("empty stack")
                return
            current = self.top
            print("--- TOP ---")
            while current is not None:
                print(f"|  {current.data}  |")
                current = current.next
            print("-----------")
        
    def __init__(self): 
        self.stack1 = self.Stack() #O(N) in space 
        self.stack2 = self.Stack() #O(N) in space
    
    def append(self, data):
        # 1. Svuota stack1 dentro stack2
        while not self.stack1.isEmpty(): #O(N)
            self.stack2.push(self.stack1.pop())
            
        # 2. Inserisci il nuovo elemento in fondo a stack1
        self.stack1.push(data)
        
        # 3. Riporta tutto da stack2 a stack1
        while not self.stack2.isEmpty(): #O(N)
            self.stack1.push(self.stack2.pop())

        self.stack1.display()
        self.stack2.display()
            
    def pop(self):
        if self.stack1.isEmpty():
            return None 
        # Ritorna l'elemento rimosso (che grazie ai cicli sopra è il primo inserito)
        return self.stack1.pop()


if __name__ == "__main__":
    x = MyQueue()

    x.append(1)
    x.append(2)
    x.append(3)

    # Ora l'ordine FIFO è garantito: il primo elemento inserito (1) uscirà per primo
    print(x.pop())  # Output: 1
    print(x.pop())  # Output: 2
    print(x.pop())