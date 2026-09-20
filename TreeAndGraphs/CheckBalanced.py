class Tree:
    class Node:
        def __init__(self, data):
            self.data=data
            self.left=None
            self.right=None
            
    def __init__(self):
        self.root=None
    def recursive_insert(self, current_node:Node, data):
        if current_node.data < data: # got to right
            if current_node.right is None:
                current_node.right=self.Node(data)
                return 
            else: # re route 
                self.recursive_insert(current_node.right, data)
        else: # go to left
            if current_node.left is None:
                current_node.left=self.Node(data)
                return
            else:
                self.recursive_insert(current_node.left, data)
    def insert(self, data):
        if self.root is None:
            self.root=self.Node(data)
        else:
            self.recursive_insert(self.root, data)
    def display(self):
        print("\n--- TREE ---")
        self._display_ricorsivo(self.root, 0, "Root: ")
        print("-----------------------------------\n")

    def _display_ricorsivo(self, nodo, livello, prefisso):
        if nodo is not None:
            print("    " * livello + prefisso + str(nodo.data))
            if nodo.left or nodo.right:
                self._display_ricorsivo(nodo.left, livello + 1, "L── ")
                self._display_ricorsivo(nodo.right, livello + 1, "R── ")
    
    def depth(self, current_node:Node):

        if current_node is None: #base case single node or leaft
            return 0
        hl=self.depth(current_node.left)
        hr=self.depth(current_node.right)

        if hl == -1 or hr ==-1 or abs(hl-hr)>1:
            return -1 #if there ia a -1 there is a propagation of it
        return max(hr, hl)+1 #otherwise propagare the height

    def check_balance(self): #Post-Order Traversal
        if self.root is None:
            return None
        if self.depth(self.root) == -1:
            return False #un balance
        else:
            return True #balance
        return self.depth(self.root) 
if __name__=="__main__":
    x=Tree()

    x.insert(4)
    x.insert(5)
    x.insert(3)
    #x.insert(6)
    #x.insert(2)
    #x.insert(8)
    #x.insert(1)

    x.display()
    print(x.check_balance())
