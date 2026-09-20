#Max Heap — insert, delete, heapify
"""
A Max Heap maintains:
parent >= children
       10
      /  \
     7    8
    / \
   3   5
"""
def heap_insert(heap, value): #log(N)
    heap.append(value)
    size=len(heap)-1 # index of the last item 
    while size >0:
        parent=(size-1)//2 # look up for the parent 
        if heap[parent]>=heap[size]:
            break
        heap[parent], heap[size]=heap[size], heap[parent]
        size=parent

# max is always heap[0]
#####################################################################
def heap_delete_max(heap):
    if not heap:
        return None
    max=heap[0]
    last=heap.pop()
    if heap:
        heap[0]=last
        i=0
        while True:
            left=i*2+1
            right=i*2+2
            largest=i
            if left<len(heap) and heap[left] > heap[largest]:
                largest=left
            if right<len(heap) and heap[right]> heap[largest]:
                largest=right

            if largest==i: # we can stop
                break
            heap[i], heap[largest]=heap[largest], heap[i]
            i=largest
#####################################################################
#Heapify
#Convert an arbitrary array into a Max Heap.
#The important optimization is to start from the last non-leaf node:
def heapify(heap):

    n = len(heap)

    for i in range(n // 2 - 1, -1, -1): # last managed index is 0 -1 is not included 
        sift_down(heap, i)

def sift_down(heap, i):
    n=len(heap)
    while True:
        left=i*2+1
        right=i*2+2
        larget=i
        if left<n and heap[left]> heap[larget]:
            larget=left
        if right<n and heap[right]> heap[larget]:
                    larget=right
        if larget==i:
             break #found out the position
        heap[i], heap[larget]=heap[larget], heap[i]
        i=larget