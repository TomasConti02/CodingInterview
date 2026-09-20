def PrintUniquePermutationsHelper(unique, anchor):
    
    if len(unique) - anchor <= 1:
        print(unique)
        return 
    
    for i in range(anchor, len(unique), 1):
        #unique[anchor], unique[i] = unique[i], unique[anchor]
        time=unique[:] ##################### Heavy O(N) 
        time[anchor], time[i]= time[i], time[anchor]
        PrintUniquePermutationsHelper(time, anchor + 1)
        #PrintUniquePermutationsHelper(unique, anchor + 1)
        #unique[anchor], unique[i] = unique[i], unique[anchor] #for the new cicle execute a swipe back 


def PrintUniquePermutations(unique_str):
    # Convert string to a list so it is mutable and easy to swap by index
    unique_list = list(unique_str)
    PrintUniquePermutationsHelper(unique_list, 0)


def main():
    unique = "ABC"
    PrintUniquePermutations(unique)


if __name__ == "__main__":
    main()