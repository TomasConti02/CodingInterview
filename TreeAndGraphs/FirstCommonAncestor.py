class Tree:

    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None
        
    def __init__(self):
        self.root = None 

    # --- NUOVI METODI PER CREARE ALBERI COMPLESSI ---
    
    def _trova_nodo(self, attuale, target):
        """Metodo di supporto per cercare un nodo specifico nell'albero"""
        if attuale is None:
            return None
        if attuale.data == target:
            return attuale
        
        sinistro = self._trova_nodo(attuale.left, target)
        if sinistro: 
            return sinistro
            
        return self._trova_nodo(attuale.right, target)

    def aggiungi_figlio(self, genitore_data, valore_nuovo, lato="L"):
        """Trova il 'genitore_data' e gli aggancia sotto un nuovo nodo a sinistra (L) o destra (R)"""
        if self.root is None:
            self.root = self.Node(valore_nuovo)
            return True
            
        genitore = self._trova_nodo(self.root, genitore_data)
        if genitore is None:
            print(f"Errore: Nodo genitore {genitore_data} non trovato!")
            return False
            
        if lato.upper() == "L":
            genitore.left = self.Node(valore_nuovo)
        else:
            genitore.right = self.Node(valore_nuovo)
        return True

    # --- I TUOI VECCHI METODI DI UTILIÀ ---
    def display(self):
        print("\n--- TREE VISUALIZATION ---")
        self._display_ricorsivo(self.root, 0, "Root: ")
        print("-----------------------------------\n")

    def _display_ricorsivo(self, nodo, livello, prefisso):
        if nodo is not None:
            print("    " * livello + prefisso + str(nodo.data))
            if nodo.left or nodo.right:
                self._display_ricorsivo(nodo.left, livello + 1, "L── ")
                self._display_ricorsivo(nodo.right, livello + 1, "R── ")


# --- IL TUO ALGORITMO DI RICERCA ANTENATO ---

def deepth(node: Tree.Node, x, path):
    if node is None:
        return False
    
    if node.data == x: 
        path.append(node.data)
        return True
    
    trovatol = deepth(node.left, x, path)
    trovator = deepth(node.right, x, path)

    if trovatol or trovator:
        path.append(node.data)
        return True
    
    return False

def CommonAncestor(node: Tree.Node, x1, x2):
    path1 = []
    path2 = []

    deepth(node, x1, path1)
    deepth(node, x2, path2)

    if len(path1) == 0 or len(path2) == 0:
        return None
    
    set_path2 = set(path2) #O(N)
    for i in path1: #O(M)
        if i in set_path2:
            return i
    return None
    
    
    

    
if __name__ == "__main__":
    t = Tree()
    
    # Creiamo un albero genealogico complesso ramificato
    #                20
    #              /    \
    #            10      30
    #           /  \       \
    #          5    15      40
    #         / \
    #        3   7
    
    t.aggiungi_figlio(None, 20)          # La radice
    t.aggiungi_figlio(20, 10, "L")       # Sotto il 20 a sinistra
    t.aggiungi_figlio(20, 30, "R")       # Sotto il 20 a destra
    
    t.aggiungi_figlio(10, 5, "L")        # Sotto il 10 a sinistra
    t.aggiungi_figlio(10, 15, "R")       # Sotto il 10 a destra
    
    t.aggiungi_figlio(30, 40, "R")       # Sotto il 30 a destra
    
    t.aggiungi_figlio(5, 3, "L")         # Sotto il 5 a sinistra
    t.aggiungi_figlio(5, 7, "R")         # Sotto il 5 a destra

    t.display()

    # --- TESTIAMO IL TUO COMMON ANCESTOR ---
    print("Cerco l'antenato comune tra 3 e 15 (Dovrebbe essere 10):")
    risultato = CommonAncestor(t.root, 3, 15)
    print("Risultato:", risultato)
    
    print("\n-------------------------\n")
    
    print("Cerco l'antenato comune tra 3 e 7 (Dovrebbe essere 5):")
    risultato2 = CommonAncestor(t.root, 3, 7)
    print("Risultato:", risultato2)