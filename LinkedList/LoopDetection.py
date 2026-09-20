class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    def print(self):
        anchor=self
        while anchor is not None:
            print(anchor.data, end=" -> " if anchor.next else "\n")
            anchor=anchor.next
    def append(self,data):
        anchor=self
        while anchor.next is not None:
            anchor=anchor.next 
        anchor.next=Node(data)
    def check_loop(self):

        anchor=self
        time=set()

        while anchor is not None:
            if anchor in time:
                return True
            time.add(anchor)
            anchor=anchor.next
        return False
if __name__ == "__main__":
    # 1. Creiamo la lista lineare iniziale: A -> B -> C -> D -> E
    x = Node("A")
    x.append("B")
    x.append("C")
    x.append("D")
    x.append("E")
    print(x.check_loop())
    
    # 2. Per creare il ciclo, dobbiamo "salvare" il riferimento al nodo C
    # e al nodo E. Lo facciamo scorrendo la lista.
    anchor = x
    nodo_C = None
    nodo_E = None
    
    while anchor is not None:
        if anchor.data == "C":
            nodo_C = anchor
        if anchor.data == "E":
            nodo_E = anchor
        anchor = anchor.next
        
    # 3. Stringiamo il cappio: facciamo puntare il 'next' di E a C
    if nodo_E and nodo_C:
        nodo_E.next = nodo_C
        print(f"Loop creato con successo: Il nodo {nodo_E.data} ora punta a {nodo_E.next.data}!")
    print(x.check_loop())