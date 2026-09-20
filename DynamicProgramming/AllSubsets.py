def all_subset(X):
    list_of_subset = [ set() ]
    for x in X:
        time = []  
        for l in list_of_subset:
            new_subset = l.copy()
            new_subset.add(x)
            time.append(new_subset)
        list_of_subset.extend(time) #merge
    return list_of_subset
def main():
    print("\nAll subset problem:")
    X = {1, 2, 3}
    result = all_subset(X)
    print(result)
if __name__ == "__main__":
    main()


""""
Initial State:
list_of_subset = [ ∅ ] (Empty set)

=========================================
Iteration 1: x = 1
=========================================
Current subsets:   [ ∅ ]
Copies + {1}:      [ {1} ]
Resulting list:    [ ∅, {1} ]

=========================================
Iteration 2: x = 2
=========================================
Current subsets:   [ ∅, {1} ]
Copies + {2}:      [ {2}, {1, 2} ]
Resulting list:    [ ∅, {1}, {2}, {1, 2} ]

=========================================
Iteration 3: x = 3
=========================================
Current subsets:   [ ∅, {1}, {2}, {1, 2} ]
Copies + {3}:      [ {3}, {1, 3}, {2, 3}, {1, 2, 3} ]
Resulting list:    [ ∅, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3} ]
"""