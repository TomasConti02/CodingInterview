#3. Count subarrays whose sum is divisible by K


def count(l, K):
    count=0
    for i in range(0, len(l)):
        s=0
        for j in range(i, len(l)):
            s+=l[j]
            if s%K==0:
                count+=1
    return count
x=[4, 5, 0, -2, -3, 1]
print(count(x, 5))
