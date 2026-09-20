class Tree:

    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None
        self.paths = {}

    def insert_BSF(self, current_node: Node, data: int):
        if current_node.data > data:
            if current_node.left is None:
                current_node.left = self.Node(data)
            else:
                self.insert_BSF(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = self.Node(data)
            else:
                self.insert_BSF(current_node.right, data)

    def insert(self, data: int):
        if self.root is None:
            self.root = self.Node(data)
            return
        else:
            self.insert_BSF(self.root, data)

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

    # Dizionario usato per capire quante volte lungo un path è stata trovata una certa somma 
    def go_in_deepth(self, current_node: Node, th: int, sum: int):

        if current_node is None:
            return 0
        
        sum += current_node.data

        somma_vecchia = sum - th
        count = self.paths.get(somma_vecchia, 0) # se non trovato diamo 0 in output

        self.paths[sum] = self.paths.get(sum, 0) + 1

        # NOTA: Rimosso 'self' dagli argomenti delle chiamate ricorsive
        # get the path number in the left branch
        count += self.go_in_deepth(current_node.left, th, sum)
        # get the path number in the right branch
        count += self.go_in_deepth(current_node.right, th, sum)
        
        # in back track clean the dictionary
        self.paths[sum] -= 1 
        return count 

    def path(self, th: int):
        self.paths = {0: 1}  # <-- CORRETTO: Adesso è un vero dizionario {chiave: valore}
        return self.go_in_deepth(self.root, th, 0)

if __name__ == "__main__":
    t = Tree()
    t.insert(3)
    t.insert(-4)
    t.insert(-1)
    t.insert(8)
    t.insert(9)
    t.insert(3)
    t.insert(100)
    t.insert(-10)
    t.display()

    # Cerchiamo i cammini che sommano a 11 (es. 3 -> 8)
    print("Cammini con somma 11:", t.path(11))
    # Cerchiamo i cammini che sommano a 20 (es. 3 -> 8 -> 9)
    print("Cammini con somma 20:", t.path(20))