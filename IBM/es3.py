3. #Relationship between two circles
"""
each circle is (x, y, r)
We need to determine:

concentric
touching
intersecting
disjoint

C1 = (x1, y1, r1)
C2 = (x2, y2, r2)
"""
import math 
def problem(c1, c2):
    x1, y1, r1=c1
    x2, y2, r2=c2

    d=math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )

    if d == 0:
        print("concentric")
        return
    
    if d == r1+r2:
        print("touching")
        return
    if d > r1+r2:
        print("disjoint")
        return
    print("intersecting")
    return

c1=(1, 2, 3)
c2=(8, 9, 3)
problem(c1, c2)