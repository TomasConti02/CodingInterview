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

        time=Node(data)
        anchor.next=time

    def palindrom(self):

        left=[] # O(N) space complexity
        right=[] # O(N) space complexity

        anchor=self

        while anchor is not None: #O(N) time complexity

            left=[ str(anchor.data) ] + left
            right= right + [ str(anchor.data) ]

            anchor=anchor.next
       
        return "".join(left)=="".join(right)
    def palindrom_stack(self):
        valori = []
        anchor = self
    
        # Riempiamo la lista normalmente O(N) tempo, O(N) spazio
        while anchor:
            valori.append(anchor.data)
            anchor = anchor.next
        # Confrontiamo la lista con il suo inverso usando lo slicing di Python
        #tanto lo copia comunque e occupa O(N)
        return valori == valori[::-1] #lista[inizio:fine:passo] -> in pratica inverte la lista 

if __name__=="__main__":
    x=Node("r")
    x.append("a")
    x.append("d")
    x.append("a")
    x.append("r")
    x.print()
    print(x.palindrom())