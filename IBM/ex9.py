#9. Return the largest palindromic substring
def palindromic(l):
    if len(l)%2!=0: # there is one center
        left=len(l)//2
        right=left
        
        while left >0 and right <len(l):
            
            left-=1
            right+=1
            if l[right]!=l[left]:
                left+=1
                right-=1
                break
            
            

        print(f"{left}  {right}")
        return l[left:right+1]
    else:
        right=len(l)//2
        left=right-1
        while left >0 and right <len(l):
                    
                    left-=1
                    right+=1
                    if l[right]!=l[left]:
                        left+=1
                        right-=1
                        break
                    
                    
        
        print(f"{left}  {right}")
        return l[left:right+1]

print(palindromic("jacecah"))
print(palindromic("aceca"))


print(palindromic("jaceecah"))
print(palindromic("aceeca"))