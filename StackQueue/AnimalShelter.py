class Stack:
    class Node:
        def __init__(self, data):
            self.data=data #it is the type
            self.next=None

    def __init__(self):
        self.top=None

    def enqueue(self,data):
        time=self.Node(data)

        time.next=self.top
        self.top=time

    def dequeueAny(self):

        if self.top is None:
            return None
        
        output=self.top.data
        self.top=self.top.next
        return output

    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def isEmpty(self):
        
        return self.top is None
    
    def dequeueDog(self):
        time=Stack()

        if self.isEmpty():
            return None

        while not self.isEmpty():

            if self.peek().startswith("dog"):
                self.dequeueAny() #
                break
            time.enqueue(self.dequeueAny())

        while not time.isEmpty():
            self.enqueue(time.dequeueAny())

    def dequeueCat(self):
        time=Stack()
        if self.isEmpty():
            return None

        while not self.isEmpty():
            if self.peek().startswith("cat"):
                self.dequeueAny() #
                break
            time.enqueue(self.dequeueAny())

        while not time.isEmpty():
            self.enqueue(time.dequeueAny())

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

if __name__=="__main__":
    x=Stack()
    x.enqueue("cat1")
    x.enqueue("cat2")
    x.enqueue("dog1")
    x.enqueue("cat3")
    x.enqueue("dog2")
    x.dequeueAny()
    x.display()
    x.enqueue("dog2")
    x.display()    
    x.dequeueDog()
    x.display()
    x.dequeueDog()
    x.display()