#1. HCF/GCD without recursion
def hcf(a, b):
    while b!=0:
        a, b=b, a%b

    return a

print(hcf(48, 18))