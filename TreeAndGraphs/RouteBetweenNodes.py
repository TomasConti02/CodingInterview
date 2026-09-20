from collections import deque

class Graph:
    class Node:
        def __init__(self, data):
            self.data = data
            self.mark = False  # Fondamentale per la BFS/DFS
            
        # Questo metodo serve per far stampare il nodo in modo leggibile (es. print(nodo))
        def __str__(self):
            return str(self.data)

    def __init__(self):
        # Mappa i dati "grezzi" (es. il numero 0) all'oggetto Node(0) corrispondente
        # In questo modo non creiamo duplicati dello stesso nodo
        self.nodes = {} 
        self.graph = {} # Chiave: oggetto Node, Valore: lista di oggetti Node
    
    def _get_or_create_node(self, data):
        """Metodo di supporto per gestire gli oggetti Node senza duplicarli"""
        if data not in self.nodes:
            nuovo_nodo = self.Node(data)
            self.nodes[data] = nuovo_nodo
            self.graph[nuovo_nodo] = []
        return self.nodes[data]

    def add(self, source_data, destination_data):
        # Recuperiamo (o creiamo) gli oggetti Node reali
        source_node = self._get_or_create_node(source_data)
        destination_node = self._get_or_create_node(destination_data)
        
        # Aggiungiamo il nodo destinazione ai vicini della sorgente
        self.graph[source_node].append(destination_node)

    def display(self):
        print("\n=== STRUTTURA DEL GRAFO (Usa oggetti Node) ===")
        # Ordiniamo in base al data dentro il nodo
        for nodo in sorted(self.graph.keys(), key=lambda n: n.data):
            print(f"● Nodo [{nodo.data}]")
            vicini = self.graph[nodo]
        
            if not vicini:
                print("   └── (Foglia)")
                continue
            
            for i, vicino in enumerate(vicini):
                prefisso = "└── " if i == len(vicini) - 1 else "├── "
                print(f"   {prefisso}punta a ➔ {vicino.data}")
        print("==============================================\n")

    def RouteBetweenNodes(self, source_data:int, destination_data:int):
        if source_data not in self.nodes or destination_data not in self.nodes:
            return False
            
        for nodo in self.graph.keys():
            nodo.mark = False
            
        start_node = self.nodes[source_data]
        end_node = self.nodes[destination_data]
        
        q = deque()
        
        start_node.mark = True
        q.append(start_node)
        
        while q:
            curr_node = q.popleft()
            
            # Abbiamo trovato il nodo di destinazione?
            if curr_node == end_node:
                return True
                
            # Esploriamo i vicini dell'oggetto corrente
            for vicino in self.graph[curr_node]:
                if not vicino.mark:
                    vicino.mark = True
                    q.append(vicino)
                    
        return False


if __name__=="__main__":
    g = Graph()
    g.add(0, 1)
    g.add(0, 2)
    g.add(1, 3)
    g.add(2, 3)
    
    g.display()
    
    # Testiamo la BFS per cercare la rotta
    print(f"Esiste un percorso da 0 a 3? -> {g.RouteBetweenNodes(0, 3)}") # True
    print(f"Esiste un percorso da 3 a 0? -> {g.RouteBetweenNodes(3, 0)}") # False (è orientato!)
    print(f"Esiste un percorso da 1 a 2? -> {g.RouteBetweenNodes(1, 2)}") # False