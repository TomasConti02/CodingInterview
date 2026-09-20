#4. Count "error" occurring three times consecutively
def error_time_cons(e): # no overlapping
    count=0
    output=0
    for log in e:
        if "error" in log:
            count+=1
            if count==3:
                count=0
                output+=1
        else:
            count=0

    return output
def error_time_cons_ov(e):
    count=0
    output=0
    for log in e:
        if "error" in log :
            count+=1
        else:
            count=0
        if count>=3:
            output+=1
    return output
logs = [
    "serverA failed",
    "serverB success",
    "error",
    "error",
    "error",
    "error",
    "",
    "error",
    "error",
    "ciao",
    "error"
]
print( error_time_cons(logs))
print( error_time_cons_ov(logs))