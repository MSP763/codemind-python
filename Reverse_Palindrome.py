def rev(n):
    s=0
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    return s
def pal(n):
    s=0
    temp=n
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==temp):
        return 1
    else:
        return 0
n=int(input())
x=rev(n)
n=x+n
if(pal(n)):
    print(n)
else:
    x=rev(n)
    n=n+x
    if(pal(n)):
        print(n)
    else:
        x=rev(n)
        n=n+x
        print(n)