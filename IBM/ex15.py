4. #Print a pattern
#Right-angled triangle
N=5
for i in range(N):
    print("*"*i)

for i in range(N, 0, -1):
    print("*"*i)
print("\n")

def piramid(v, num):
    if v>=0:
        v=v-1
        num+=1
        piramid( v , num)
        num+=1
        v+=1
        print(" "*num+"*"*((v*2)-1))

piramid(5,0)