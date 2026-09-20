class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.root = None

    def create_minimal_bst(self, array_of_data):
        if not array_of_data:
            return None
        
        array_ordinato = sorted(array_of_data) #O(NlogN) and space O(N)
        self.root = self._build_tree_ricorsivo(array_ordinato)

    def _build_tree_ricorsivo(self, array_ordinato): #Pre-Order Traversal
        if not array_ordinato: #empty array => leaft
            return None
        
        middle = len(array_ordinato) // 2 
        current_node = self.Node(array_ordinato[middle])
        
        current_node.left = self._build_tree_ricorsivo(array_ordinato[:middle])
        current_node.right = self._build_tree_ricorsivo(array_ordinato[middle+1:])
        
        # Restituisce il nodo appena creato al chiamante (il genitore)
        return current_node

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


if __name__ == "__main__":
    t = Tree()
    # Array disordinato di prova
    array = [13, 4, 56, 7, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Creiamo l'albero
    t.create_minimal_bst(array)
    
    # Ora la struttura si stamperà perfettamente!
    t.display()