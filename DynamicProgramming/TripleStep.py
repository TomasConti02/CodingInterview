def paths(p, cache):

    if p ==1 :
        return 1
    elif p==2:
        return 2
    elif p==3:
        return 4
    elif p in cache:
        return cache[p]
    
    child1=paths(p-1, cache)
    child2=paths(p-2, cache)
    child3=paths(p-3, cache)
    sum=child1+child2+child3
    cache.setdefault(p, sum)
    return sum

def main():
    n=4
    cache={}
    output=paths(n,cache)
    print(output)

if __name__=="__main__":
    main()