

def helper(A, x, y):

    mid=(y+x)//2

    print(f"\n {A[mid]}  ---- {mid}")
    if A[mid]==mid:
        return mid

    print(f"{x}, {y}")
    if x >= y:
        print(f"{x}, {y}")
        return - 1
    
    if A[mid] > mid:
        return helper(A, x, mid-1) # left 
    else:
        return helper(A, mid+1, y) #right 


def find_out(x):
    if x is None or len(x)==0:
        return None
    return helper(x, 0, len(x))

# att i can no do this x[mid:]!!!!!!!!!!!!! indexing change, keep x and work with nidex only 
def main():
    print("ciao")
       #0,   1,  2, 3,  4, 5, 6, 7, 8 ,9, 10, 11 ]
    #A=[-10, -5, -4, 2 , 3, 4, 5, 6, 8, 11, 12, 20 ]
    #A=[-2, -1, 2]
    #A=[0]
    A=[-1, 0, 9]
    #A=[]
    #magic number can not be negative
    print(find_out(A))
if __name__=="__main__":
    main()

    # 5 , 6, 7, 8, 
    # 6
    # 5, 6, 7, 8, 
    #4