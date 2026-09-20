#Convert an IPv4 address to IPv6 address format
"""

Example
Input: 192.168.1.1
Output: ::ffff:c0a8:0101

An IPv4 address has 4 decimal bytes:

192.168.1.1

Convert each byte to hexadecimal:

192 -> c0
168 -> a8
1   -> 01
1   -> 01

So:

c0a8:0101

An IPv4-mapped IPv6 address is:

::ffff:c0a8:0101
"""
#:02x ->hexadecimal string formatting
def ipv4_to_ipv6(s):
    tokens=s.split(".")
    print(tokens)
    output=[]
    for t in tokens:
        output.append(f"{int(t):02x}")
    print(output)
    return "::ffff:"+output[3]+output[2]+":"+output[1]+output[0]



print(ipv4_to_ipv6("192.168.1.1"))