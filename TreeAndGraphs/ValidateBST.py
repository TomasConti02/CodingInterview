class Tree:
    class Node:
        def __init__(self, data):
            self.data=data
            self.right=None 
            self.left=None
    def __init__(self):
        self.root=None
    
    def recursive_inserting(self, current_node:Node, data):
        if current_node.data > data: #go to the left 
            if current_node.left is None:
                current_node.left=self.Node(data)
                return
            else:
                self.recursive_inserting(current_node.left, data)
        else: # go to the right
            if current_node.right is None:
                current_node.right=self.Node(data)
                return
            else:
                self.recursive_inserting(current_node.right, data)
    def insert(self, data):
        if self.root is None:
            self.root=self.Node(data)
        else:
            self.recursive_inserting(self.root, data)


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
def recursive(node):

    if node is None:
        return None
    
    data_left=recursive(node.left)
    data_right=recursive(node.right)

    if data_left ==-1 or data_right ==-1:
        return -1 #upfward
    
    if data_left is None and data_right is None: #leaft
        return node.data
    
    if data_right is not None and node.data > data_right:
        return -1 #error
    elif data_left is not None and node.data < data_left:
        return -1
    else:
        return node.data
    
def BST_check(node):
    if node.root is None:
        return True
    result=recursive(node.root)
    if result == -1:
        return False
    else:
        return True
    # in case of failure propagate the errore to the root


if __name__=="__main__":
    x=Tree()
    x.insert(5)
    x.insert(1)
    x.insert(6)
    x.insert(7)
    x.display()

    print(BST_check(x))