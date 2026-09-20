class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        anchor = self
        while anchor.next is not None:
            anchor = anchor.next
        new = Node(data)
        anchor.next = new

    def print(self):
        anchor = self
        while anchor is not None:
            print(anchor.data, end=" -> " if anchor.next else "\n")
            anchor = anchor.next

    def Partition(self, x): 
        """
        Versione originale: O(N) tempo, O(N) spazio.
        Crea nuovi nodi per ogni elemento.
        """
        anchor = self
        smaller = Node(-1)
        anchor_smaller = smaller
        equal = Node(-1)
        anchor_equal = equal
        bigger = Node(-1)
        anchor_bigger = bigger

        while anchor is not None:
            time = Node(anchor.data)
            if anchor.data < x:
                smaller.next = time
                smaller = smaller.next
            elif anchor.data > x:
                bigger.next = time
                bigger = bigger.next
            elif anchor.data == x:
                equal.next = time
                equal = equal.next
            anchor = anchor.next
        
        # Concatenazione: Smaller -> Equal -> Bigger
        smaller.next = anchor_equal.next
        equal.next = anchor_bigger.next
        
        return anchor_smaller.next

    def Partition2(self, x):
        """
        Versione ottimizzata: O(N) tempo, O(1) spazio extra.
        Riutilizza i nodi esistenti spostando i puntatori.
        """
        smaller_head = Node(-1)
        equal_head = Node(-1)
        bigger_head = Node(-1)

        s = smaller_head
        e = equal_head
        b = bigger_head

        curr = self 
        while curr:
            next_node = curr.next 
            curr.next = None # "Sganciamo" il nodo dalla vecchia lista
            
            if curr.data < x:
                s.next = curr
                s = s.next
            elif curr.data == x:
                e.next = curr
                e = e.next
            else:
                b.next = curr
                b = b.next
            curr = next_node 

        # Concatenazione intelligente
        # Se non ci sono 'equal', colleghiamo 'smaller' direttamente a 'bigger'
        if equal_head.next:
            s.next = equal_head.next
            e.next = bigger_head.next
        else:
            s.next = bigger_head.next

        return smaller_head.next

if __name__ == "__main__":
    # Creazione lista di test
    x = Node(3)
    x.append(5)
    x.append(8)
    x.append(5)
    x.append(10)
    x.append(2)
    x.append(1)
    
    print("Lista Originale:")
    x.print()
    
    # Test versione 1 (Copia)
    print("\nRisultato Partition (O(N) spazio):")
    res1 = x.Partition(5)
    res1.print()
    
    # Test versione 2 (In-place)
    # Nota: Usiamo res1 come base o ricreiamo x perché Partition2 distrugge 
    # i legami originali di x.
    print("\nRisultato Partition2 (O(1) spazio):")
    res2 = res1.Partition2(5)
    res2.print()
"""
def Partition_Ultimate(self, x):
    # Tre teste dummy
    sh, eh, bh = Node(0), Node(0), Node(0)
    # Tre puntatori correnti
    s, e, b = sh, eh, bh

    curr = self
    while curr:
        if curr.data < x:
            s.next = curr
            s = s.next
        elif curr.data == x:
            e.next = curr
            e = e.next
        else:
            b.next = curr
            b = b.next
        curr = curr.next

    # Cruciale: interrompiamo l'ultimo legame per evitare cicli
    b.next = None
    
    # Concatenazione a cascata:
    # Colleghiamo gli uguali ai maggiori
    e.next = bh.next
    # Colleghiamo i minori agli uguali
    s.next = eh.next

    return sh.next
"""