class Stack:
    class Node:
        def __init__(self, data):
            self.data=data
            self.next=None

    def __init__(self):
        self.top=None
        

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
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    def isEmpty(self):
        return self.top is None
    
def sort_stack(stack:Stack):
    time=Stack()
    
    if stack.isEmpty():
        return None
    
    data=stack.pop()
    time.push(data)

    while not stack.isEmpty: #until input stack is empty
        data=stack.pop()

        th=time.peek()
        if data < th:
            time.push() # keep the order
        else:
            count=0
            while not time.isEmpty() or time.peek() > data:
                stack.push(time.pop())
                count+=1
            time.push(data)
            for i in range(count):
                time.push(stack.pop())

    while not time.isEmpty():
        print("caio")
        stack.push(time.pop())



if __name__=="__main__":
    x=Stack()
    x.push(1)
    x.push(2)
    x.push(3)
    print(x.pop())
    print(x.pop())
    print(x.pop())
    x.push(5)
    x.push(4)
    x.push(3)
    x.push(1)
    sort_stack(x)
    print(x.pop())
    print(x.pop())
    print(x.pop())
    print(x.pop())
    