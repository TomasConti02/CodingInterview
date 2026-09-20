1. #Greedy resource allocation

resources = [2, 3]
tasks     = [1, 2, 4]

resources = [1, 5]
tasks     = [2, 3]

def max(r, t):
    r.sort()
    print(r)
    t.sort()
    print(t)
    i=0
    j=0
    c=0
    while i<len(r) and j<len(t):
        if r[i]>=t[j]:
            c+=1
            j+=1
        i+=1
    return c

print(max(resources, tasks))