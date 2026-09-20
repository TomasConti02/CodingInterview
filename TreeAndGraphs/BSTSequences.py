class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None
            
    def __init__(self):
        self.root = None 
        
    def insert_BST(self, current_node: Node, data):
        if current_node.data > data:  # go to the left
            if current_node.left is None:
                current_node.left = self.Node(data)
                return
            else:
                self.insert_BST(current_node.left, data)
        else:  # go to the right
            if current_node.right is None:
                current_node.right = self.Node(data)
                return
            else:
                self.insert_BST(current_node.right, data)

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self.insert_BST(self.root, data)

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

    def go_depth(self, current_node: Node, data, targret):
        if current_node is None:
            return False
        
        if current_node.data == targret:
            if current_node.left is not None:
                data.append(current_node.left.data)
            if current_node.right is not None:
                data.append(current_node.right.data)
            return True  # stop recursion 
        else:
            return self.go_depth(current_node.left, data, targret) or self.go_depth(current_node.right, data, targret)

    def sons(self, target):
        result = []
        trovato = self.go_depth(self.root, result, target)
        if not trovato:
            return None
        return result


def create(tree: Tree, paths: list):
    """
    Trova tutte le sequenze di array possibili che generano il BST dato.
    Riempie la lista 'paths' passata come argomento.
    """
    if tree.root is None:
        return None

    def backtrack(percorso_corrente, disponibili):
        # CASO BASE: Se non ci sono più scelte disponibili,
        # significa che abbiamo inserito tutti i nodi dell'albero!
        if not disponibili:
            paths.append(percorso_corrente)
            return None

        # Proviamo ad esplorare ogni numero attualmente selezionabile
        for valore in disponibili:
            # 1. Creiamo un nuovo cammino aggiungendo il valore corrente
            nuovo_percorso = percorso_corrente + [valore]
            
            # 2. Creiamo una nuova lista di disponibili escludendo il valore appena usato
            nuovi_disponibili = [v for v in disponibili if v != valore]
            
            # 3. Usiamo il TUO metodo .sons() per trovare i figli del valore appena preso
            figli = tree.sons(valore)
            if figli:  # Se ha figli (quindi non è None e non è [])
                for f in figli:
                    nuovi_disponibili.append(f)
            
            # 4. Ricorsione: passiamo le nuove liste clonate alla chiamata successiva
            backtrack(nuovo_percorso, nuovi_disponibili)

    # Facciamo partire l'algoritmo passando una lista vuota e la radice come unica scelta iniziale
    backtrack([], [tree.root.data])


if __name__ == "__main__":
    # Creiamo l'albero di esempio [5, 4, 6, 1, 2, 7, 8]
    x = Tree()
    data = [4,2,5,1]
    for i in data:
        x.insert(i)
        
    x.display()

    # Prepariamo la lista che riceverà tutti i percorsi validi
    paths = []
    
    # Eseguiamo la funzione
    create(x, paths)
    
    # Stampiamo i risultati
    print(f"Numero totale di sequenze valide generate: {len(paths)}")
    print("\nEcco le prime 10 sequenze trovate:")
    for p in paths[:10]:
        print(f"  {p}")