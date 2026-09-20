import math
#2. Find the GCD of an array
def GCD(l):
    max=l[0]

    for i in l[1:]:

        max=math.gcd(max, i)
        print(max)
        if max==1:
            return -1

    if max==1:
        return -1
    else:
        return max

l=[8,  48, 12 ]
print(GCD(l))