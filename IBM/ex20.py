#5. Print all duplicates in an array
def dup(l):
    s=set()
    out=[]

    for i in l:
        if not i in s:
            s.add(i)
        else:
            out.append(i)

    return out


print(dup([1, 2, 3, 2, 4, 1, 5]))