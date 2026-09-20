
def recursion( H, W, r):

    if  W==1:
        return H
    
    half= W // 2

    print(f"\n W = {W}---- half = {half}")
    """
    if W - (half*2) > 0:
        r[0]+=1
    """
    back=recursion(H, half, r)
    if W - (half*2) > 0:
        return back+back+H
    else:

        return back+back

def sum(H, W):
    r=[0]
    result=recursion(H, W, r)
    print(r[0])
    """
    if r[0]==1:
        result+=H
    """
    print(result)

def main():
    print("ciao")
    H=10
    W=4
    print( sum(H, W) )

if __name__=="__main__":
    main()