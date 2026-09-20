#Simple if-else logic
def largest(a, b, c):
    if a>b and a>c:
        return a
    elif b >a and b>c:
        return b
    else:
        return c

print(largest(1, 23, 3))

"""
90+ → A
80–89 → B
70–79 → C
60–69 → D
<60 → F
"""
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(grade(1))