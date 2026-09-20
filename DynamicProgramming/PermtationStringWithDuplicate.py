
def PrintPermutationsWithDuplicatesHelper(x, anchor, cache):

    if len(x)-anchor <=1:
        result="".join(x)
        cache.add(result)
        print(result)
        return None 
    
    for i in range(anchor, len(x), 1):

        x[anchor], x[i] =x[i], x[anchor]

        if "".join(x) not in cache:

            PrintPermutationsWithDuplicatesHelper(x, (anchor+1), cache)

        x[i], x[anchor] =x[anchor], x[i]


def PrintPermutationsWithDuplicates(x):
    cache=set()# set of results
    x=list(x)
    PrintPermutationsWithDuplicatesHelper(x, 0, cache)

def main():
    x="AAB"
    PrintPermutationsWithDuplicates(x)
    
if __name__=="__main__":
    main()