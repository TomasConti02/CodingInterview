#8. Can a string be formed by concatenating words?
"""
s = "leetcode"
words = ["leet", "code"]
"""
from collections import deque
def concatenating(s, w):
    words=set(w)
    q=deque([0]) # is required a iterable obj as input !!! 
    visited=set()
    while q:
        start=q.popleft()
        if start in visited:
            continue
        visited.add(start)

        for end in range(start+1, len(s)+1):
            sub=s[start:end]
            if sub in words:
                if end==len(s):
                    return True
                q.append(end)
    return False



s = "leetcode"
words = ["leet", "code"]
print(concatenating(s, words))