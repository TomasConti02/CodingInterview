#11. Check whether a sentence is a pangram
def pangram(l):
    s=set()
    for c in l.lower():
        if c.isalpha():
            s.add(c)
    return len(s)==26

print(pangram("The quick brown fox jumps over the lazy dog"))