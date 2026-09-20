

def check_validity(x): #O(N)
    #print(x)

    s=[]

    for val in x:

        if val[0] == "(": #open 
            s.append(val)

        elif val[0] == ")": #close
            if len(s)==0:
                return False
            s.pop()
    if len(s)==0:
        return True
    elif s.pop()==")":
        return False
    return True
def check_close(x): #O(N)
    #print(x)

    s=[]

    for val in x:
        if val[0] == "(": #open 
            s.append(val)
        elif val[0] == ")": #close
            if len(s)==0:
                return False
            s.pop()

    if len(s)==0:
        return True
    return False
def print_parentesis_helper(state, depth):
    
    if not check_validity(state):
        return None
    
    if depth == 0:
        if check_close(state):
            print( "".join(state) )
        return None
    
    depth=depth-1

    print_parentesis_helper(state+["("], depth) 
    print_parentesis_helper(state+[")"], depth)

def print_parentesis(depth):
    l=[]
    print_parentesis_helper(l, depth)

def main():
    print_parentesis(6)

if __name__=="__main__":
    main()