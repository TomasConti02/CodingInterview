#2. Count triplets whose sum is divisible by K
import itertools

arr = [1, 2, 3, 4, 5]
K=3
print(list(itertools.combinations(arr, 3)))
comb=list(itertools.combinations(arr, 3))
count=0
for c in comb:
    if (c[0]+c[1]+c[2]) % K==0:
        count+=1
print(count)