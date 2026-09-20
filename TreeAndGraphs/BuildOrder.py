from collections import deque 
class Graph:
    def __init__(self):
        self.nodes = set()
        self.graph = {}  # Dizionario delle adiacenze: nodo -> lista di nodi collegati
        self.visited=set()

    def add_node(self, node):
        """Inizializza il nodo nel dizionario se non esiste, garantendo che abbia la sua lista"""
        if node not in self.nodes:
            self.nodes.add(node)
            self.graph[node] = []

    def append(self, source, destination):
        """Crea un legame orientato da source a destination"""
        # 1. Garantiamo che entrambi i nodi esistano nella struttura dati
        self.add_node(source)
        self.add_node(destination)
        # 2. Aggiungiamo il collegamento orientato
        self.graph[source].append(destination)
            
    def display(self):
        print("\n--- STATO DEL GRAFO ---")
        print(f"Tutti i nodi registrati: {self.nodes}")
        print("Mappa delle adiacenze (chi punta a chi):")
        for nodo, vicini in self.graph.items():
            print(f"  {nodo} ──> {vicini}")
        print("------------------------\n")

    def DFS(self, current_node, path):

        #if len(self.graph.get(current_node))==0: #leaft O(1)
            #return current_node 
        if current_node is None or current_node in self.visited:
            return None
        
        self.visited.add(current_node)

        #path.append(current_node)

        for n in self.graph.get(current_node):
            print("\n"+n)
            if n not in self.visited:

                self.DFS(n, path)

        path.appendleft(current_node)

    def path(self):
        #find out the free starting pointer that do not have any dependency
        starter=self.nodes.copy()
        # trovar una chiave che non compaia nei values degli altri 
        for key, values in self.graph.items():
            for v in values:
                if v in starter:
                    starter.remove(v)
        if len(starter)==0:
            return None
        print("started ->"+str(starter))
        #ogni started è un nodo non richiesto da altri nodi prima di partire 
        de = deque() 
        for s in starter:
            self.DFS(s, de)
        print(de)
            

if __name__ == "__main__":
    g = Graph()
    g.append("a", "d")
    g.append("f", "b")
    g.append("b", "d")
    g.append("f", "a")
    g.append("d", "c")
        
    g.display()

    g.path()
"""
attenzione all'ordine a d serve prima la visita di a !!!!!!!!!
       f
      / \
     v   v
     b   a
     \   /
      v v
       d
       |
       v
       c
"""