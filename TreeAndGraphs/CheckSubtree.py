class Tree:

    class Node:
        def __init__(self, data):
            self.data=data
            self.right=None
            self.left=None

    def __init__(self):
        self.root=None

    def insert_BST(self, current_node, data):
        if current_node.data > data: # go to the left 
            if current_node.left is None:
                current_node.left=self.Node(data)
                return
            else:
                self.insert_BST(current_node.left, data)
            
        else: # go to the right 
            if current_node.right is None:
                current_node.right=self.Node(data)
                return
            else:
                self.insert_BST(current_node.right, data)

    def insert(self, data):
        if self.root is None:
            self.root=self.Node(data)
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

# Manteniamo la struttura delle tue funzioni corrette precedenti
def starting_node(node: Tree.Node, nodes, target):
    if node is None:
        return None 
    if node.data == target:
        nodes.append(node)
    starting_node(node.left, nodes, target)
    starting_node(node.right, nodes, target)

def are_equale(node1: Tree.Node, node2: Tree.Node):
    if node1 is None and node2 is None:
        return True
    
    if node1 is None or node2 is None:
        return False
    
    if node1.data != node2.data:
        return False
    
    return are_equale(node1.left, node2.left) and are_equale(node1.right, node2.right)
    
def check_subtree(t1: Tree, t2: Tree):
    if t2.root is None: 
        return True  # L'albero vuoto è sempre un sottoalbero
    if t1.root is None: 
        return False
        
    starting_nodes = []
    starting_node(t1.root, starting_nodes, t2.root.data)
    
    for starter in starting_nodes:
        if are_equale(starter, t2.root):
            return True
    return False


# ==========================================
# TIMING & ROBUST TESTING SUITE
# ==========================================
def run_robust_tests():
    print("🚀 Avvio della suite di testing robusto...\n")

    # ----------------------------------------------------
    # CASE 1: Valori identici ma strutture strutturalmente diverse
    # T1 (Sbilanciato a sinistra):   3      T2 (Sbilanciato a destra): 3
    #                               /                                  \
    #                              2                                    2
    # ----------------------------------------------------
    t1_1, t2_1 = Tree(), Tree()
    # Costruiamo manualmente o forzando l'ordine per cambiare struttura
    t1_1.insert(3); t1_1.insert(2) 
    t2_1.insert(2); t2_1.insert(3) # Questo inserimento crea 2 come Root e 3 come Right
    # Per avere 3 come root e 2 a destra in T2, lo inseriamo diversamente:
    t2_1 = Tree()
    t2_1.root = Tree.Node(3)
    t2_1.root.right = Tree.Node(2)
    
    assert check_subtree(t1_1, t2_1) == False, "Fallito Caso 1: Stessi valori ma geometrie diverse!"
    print("✅ Caso 1 Superato: Geometrie diverse con stessi valori isolate correttamente.")


    # ----------------------------------------------------
    # CASE 2: Duplicati multipli in T1 (Il "Falso Amico")
    # T1 ha DUE nodi con valore '5'. Il primo ha figli diversi, il secondo è quello buono.
    # ----------------------------------------------------
    t1_2 = Tree()
    # Costruzione manuale per forzare duplicati strutturati
    t1_2.root = Tree.Node(10)
    t1_2.root.left = Tree.Node(5)       # Primo '5' (Sbagliato)
    t1_2.root.left.left = Tree.Node(1)
    
    t1_2.root.right = Tree.Node(20)
    t1_2.root.right.left = Tree.Node(5) # Secondo '5' (Quello CORRETTO)
    t1_2.root.right.left.left = Tree.Node(3)
    t1_2.root.right.left.right = Tree.Node(7)

    t2_2 = Tree()
    t2_2.insert(5); t2_2.insert(3); t2_2.insert(7) # Cerca il '5' con figli 3 e 7
    
    assert check_subtree(t1_2, t2_2) == True, "Fallito Caso 2: Non ha trovato il duplicato corretto!"
    print("✅ Caso 2 Superato: Gestione dei duplicati multipli funzionante.")


    # ----------------------------------------------------
    # CASE 3: T2 è quasi identico, ma a T1 manca un pezzo finale (Troncamento)
    # T1 ha solo (5 -> 3), ma T2 si aspetta (5 -> 3 e 7)
    # ----------------------------------------------------
    t1_3, t2_3 = Tree(), Tree()
    t1_3.insert(5); t1_3.insert(3)
    t2_3.insert(5); t2_3.insert(3); t2_3.insert(7)
    
    assert check_subtree(t1_3, t2_3) == False, "Fallito Caso 3: T1 è più piccolo della richiesta di T2!"
    print("✅ Caso 3 Superato: Rilevato albero T1 incompleto rispetto alla richiesta di T2.")


    # ----------------------------------------------------
    # CASE 4: Estensioni profonde in T1 (T2 finisce prima, ma T1 continua)
    # T1 ha (5 -> 3 -> 1), T2 ha solo (5 -> 3). Deve fallire perché NON è un sottoalbero identico fino alle foglie terminali di T2.
    # Nota: Nella definizione standard di "Subtree" (Cracking the Coding Interview), 
    # se T2 è un sottoalbero, TUTTI i nodi da quel punto in giù devono essere IDENTICI a T1. 
    # Se T1 continua sotto, are_equale deve restituire False quando T2 finisce ma T1 ha ancora roba.
    # ----------------------------------------------------
    t1_4, t2_4 = Tree(), Tree()
    t1_4.insert(5); t1_4.insert(3); t1_4.insert(1)
    t2_4.insert(5); t2_4.insert(3)
    
    assert check_subtree(t1_4, t2_4) == False, "Fallito Caso 4: T1 continua sotto ma T2 è finito!"
    print("✅ Caso 4 Superato: Riconosciuto che T1 ha nodi extra non presenti in T2.")


    # ----------------------------------------------------
    # CASE 5: Albero T2 vuoto o alberi con nodi singoli uguali
    # ----------------------------------------------------
    t1_5, t2_5 = Tree(), Tree()
    assert check_subtree(t1_5, t2_5) == True, "Fallito Caso 5a: Due alberi vuoti devono dare True"
    
    t1_5.insert(10)
    assert check_subtree(t1_5, Tree()) == True, "Fallito Caso 5b: T2 vuoto deve sempre essere True"
    
    t2_5.insert(10)
    assert check_subtree(t1_5, t2_5) == True, "Fallito Caso 5c: Nodi singoli identici devono dare True"
    
    print("✅ Caso 5 Superato: Edge cases su alberi vuoti e nodi singoli superati.")

    print("\n🎉 COMPLIMENTI! Il tuo algoritmo ha superato tutti i test di robustezza!")

if __name__ == "__main__":
    run_robust_tests()