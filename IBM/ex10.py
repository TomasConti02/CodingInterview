#10. Check if a sentence is grammatically correct
def check(s):
    if s[0]!=s.upper()[0]:
        return False
    if s[-1]not in "?!.":
        return False
    print(s[:-1])
    if len(s[:-1].split()) != s.count(" ")+1:
        return False
    return True

s="Fello how are you?"
print(check(s))