x=input().split()
c=min(x[len(x)-1])
c1=chr(ord(c)+32)
if c1 in x[len(x)-1]:
    print(c1)
else:
    print(c)