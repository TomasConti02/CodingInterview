import collections

class Tree:

    class Node:

        def __init__(self, data):
            self.data=data
            self.left=None
            self.right=None
        
    def __init__(self):
        self.root=None
        self.layers=None

    def binary_search_tree(self, current_node:Node, data):
        if current_node.data < data: # lets go to right
            if current_node.right is None: #insert
                current_node.right=self.Node(data)
                return
            else: #re rout
                self.binary_search_tree(current_node.right, data)
        else:
            if current_node.left is None: #insert
                current_node.left=self.Node(data)
                return
            else: #re route
                self.binary_search_tree(current_node.left, data)


    def insert(self, data):
        if not self.root:
            self.root=self.Node(data)
        else:
            self.binary_search_tree(self.root, data)
    def display(self):
        print("\n--- TREE (BST) ---")
        self._display_ricorsivo(self.root, 0, "Root: ")
        print("-----------------------------------\n")

    def _display_ricorsivo(self, nodo, livello, prefisso):
        if nodo is not None:
            print("    " * livello + prefisso + str(nodo.data))
            if nodo.left or nodo.right:
                self._display_ricorsivo(nodo.left, livello + 1, "L── ")
                self._display_ricorsivo(nodo.right, livello + 1, "R── ")

    def go_depth(self, current_node:Node, depth:int):

        if current_node is None: #base case
            return None
        
        if not self.layers.get(depth):
            self.layers[depth]=collections.deque([current_node.data])
        else:
            self.layers[depth].append(current_node.data)

        depth+=1

        self.go_depth(current_node.left, depth)
        self.go_depth(current_node.right, depth)

    def list_of_depth(self):

        self.layers={} #dictionary
        depth=0

        self.go_depth(self.root, depth)

        return self.layers


if __name__=="__main__":
    x=Tree()

    x.insert(1)

    x.insert(3)
    x.insert(0)

    x.insert(2)
    x.insert(-1)

    x.insert(5)
    x.insert(10)

    x.display()

    print(x.list_of_depth())

        