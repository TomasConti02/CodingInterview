#use a list of node and save for each node also the position in the list 
#or a size for each node usad to drive the get random
import collections
import random

class Tree:

    class Node:
        def __init__(self, data):
            self.data=data
            self.right=None
            self.left=None

    def __init__(self):

        self.root=None
        self.list_nodes=[] #removing a data can cost O(N) 

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

    def insert_BST(self, current_nodes:Node, data): #O(log(N))

        if current_nodes.data > data:

            if current_nodes.left is None:
                current_nodes.left=self.Node(data)
                return
            else:
                self.insert_BST(current_nodes.left, data)

        else:

            if current_nodes.right is None:
                current_nodes.right=self.Node(data)
                return
            else:
                self.insert_BST(current_nodes.right, data)

    def insert(self, data): #O(log(N))

        if self.root is None:
            self.root=self.Node(data)
            self.list_nodes.append(data)
            return
        else:
            self.list_nodes.append(data)
            self.insert_BST(self.root, data)
    
    # Get inorder successor (smallest in right subtree)
    def getSuccessor(self, curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    def delete_deeph(self, current_node:Node, data):
        if current_node is None:
            return current_node
        if current_node.data > data:
            current_node.left=self.delete_deeph(current_node.left, data)
        elif current_node.data < data:
            current_node.right=self.delete_deeph(current_node.right, data)
        #here nothing change, only node re assign
        # here we ho if current_node.data ==  data
        else: 
            # in case of 0 or 1 child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            #there are both the child 
            succ=self.getSuccessor(current_node)
            current_node.data=succ.data
            current_node.right=self.delete_deeph(current_node.right, succ.data) ##########
        return current_node

    def delete(self, data): #O(log(N))
        self.root=self.delete_deeph(self.root, data)
        self.list_nodes.remove(data) #O(N) !!!!!!!!!!!!!
    
    def deeph(self, current_node: Node, data):
        # Caso base 1: siamo arrivati in fondo e non abbiamo trovato nulla
        if current_node is None:
            return False
    
        # Caso base 2: abbiamo trovato il nodo!
        if current_node.data == data:
            return True
    
        # Se il dato è più piccolo, cerchiamo a sinistra e "andiamo a rimbalzo" con il return
        if current_node.data > data:
            result=self.deeph(current_node.left, data)
            #return self.find(current_node.left, data) più semplice tanto propago 
            if result == True:
                return True
            else:
                return False
        else:
            result=self.deeph(current_node.right, data)
            #self.find(current_node.right, data) semplice tanto propago
            if result == True:
                return True
            else:
                return False
    def find(self, data): #O(log(N))
        return self.deeph(self.root, data)
    
    def getRandomNode(self): #O(log(N))
        index=len(self.list_nodes)
        node=self.list_nodes[random.random(index)]
        return node

if __name__=="__main__":
    t=Tree()
    t.insert(5)
    t.insert(1)
    t.insert(6)
    t.insert(0)
    t.display()
    print(t.find(3))
    t.delete(1)
    t.display()