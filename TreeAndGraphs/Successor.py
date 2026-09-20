class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None 
            self.parent = None 
        def set_parent(self, parent):
            self.parent = parent

    def __init__(self):
        self.root = None
        self.nodes = set()

    def get_nodes(self):
        return self.nodes
    
    def display(self):
        print("\n--- TREE ---")
        self._display_ricorsivo(self.root, 0, "Root: ")
        print("-----------------------------------\n")

    def _display_ricorsivo(self, nodo, livello, prefisso):
        if nodo is not None:
            print("    " * livello + prefisso + str(nodo.data))
            if nodo.left or nodo.right:
                self._display_ricorsivo(nodo.left, nivel_plus_1 := livello + 1, "L── ")
                self._display_ricorsivo(nodo.right, nivel_plus_1, "R── ")

    def BST(self, current_node: Node, data):
        if current_node.data > data: # left
            if current_node.left is None:
                tmp = self.Node(data)
                self.nodes.add(tmp)
                tmp.set_parent(current_node)
                current_node.left = tmp
                return
            else:
                self.BST(current_node.left, data)
        else: # right
            if current_node.right is None:
                tmp = self.Node(data)
                self.nodes.add(tmp)
                tmp.set_parent(current_node)
                current_node.right = tmp
                return
            else:
                self.BST(current_node.right, data)

    def insert(self, data):
        if self.root is None:
            tmp = self.Node(data)
            self.nodes.add(tmp)
            self.root = tmp
        else:
            self.BST(self.root, data)


# --- FUNZIONI DI SUPPORTO PER IL SUCCESSORE ---

def _min_value_node(node: Tree.Node):
    """Trova il nodo con il valore minimo partendo da un determinato nodo (va tutto a sinistra)"""
    current = node
    while current.left is not None:
        current = current.left
    return current

# ci affidiamo alla topologia del tree, a destra tutto quello piu grande e sinistra piu piccolo
#Quando cerchi il successore in-order (il numero immediatamente successivo), stai geometricamente cercando il punto più vicino muovendoti verso destra.

#Caso 1: C'è una strada a destra (Il nodo ha un figlio destro)
#Il movimento geometrico: Fai un passo a destra, e poi scendi tutto a sinistra finché trovi un vicolo cieco (un nodo senza figlio sinistro).

#Caso 2: La strada a destra è bloccata (Il nodo NON ha un figlio destro)
def successor(node: Tree.Node):
    if node is None:
        return None
    
    # CASO 1: Il nodo ha un sottoalbero destro.
    # Il successore è il nodo più a sinistra nel sottoalbero destro.
    if node.right is not None:
        #no recursion tanto devo andare dritto in basso
        return _min_value_node(node.right) #passo a destra e poi fino in fondo
    
    # CASO 2: Il nodo NON ha un sottoalbero destro.
    # Risaliamo l'albero verso i parent finché non troviamo un nodo che è FIGLIO SINISTRO di suo padre.
    #Ti fermi solo quando arrivi a un padre provenendo da sinistra (ovvero, tu sei il suo figlio sinistro).
    p = node.parent
    while p is not None and node == p.right: #continuo fino a che non sono stato prodotto da un figlio a destra e diverso da null
        node = p
        p = p.parent
        
    return p # Se arriviamo in cima alla radice e p diventa None, significa che il nodo era il massimo assoluto dell'albero.


if __name__ == "__main__":
    albero = Tree()
    albero.insert(5)
    albero.insert(1)
    albero.insert(7)
    albero.insert(0)
    albero.insert(2)
    albero.insert(6)
    albero.insert(8)

    albero.display()

    # Testiamo TUTTI i nodi per vedere se funziona alla perfezione
    # Usiamo un nome diverso da 'x' per non sovrascrivere l'albero
    for nodo_corrente in sorted(albero.get_nodes(), key=lambda n: n.data):
        succ = successor(nodo_corrente)
        out_val = succ.data if succ else "None (È il valore massimo!)"
        print(f"Il successore di {nodo_corrente.data} è -> {out_val}")