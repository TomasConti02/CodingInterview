#2. Find the length of the last word
"""
"   Hello   World   "

Output:
5
"""
def lenght_final_word(l):
    tokens=l.split() #split manage multiple space 
    return len(tokens[-1]) #-1 is the last word
print(lenght_final_word("   Hello   World  "))