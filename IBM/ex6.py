#6. Check if a pair with a given sum exists
def pair(l, target):

    s=set()

    for x in l:
        if not x in s:

            s.add((target-x))
        else:
            return True
        
    return False


nums = [2, 7, 11, 15]
target = 9
print(pair(nums, target))