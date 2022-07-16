def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
a=int(input())
k=10000
g=1
for i in range(1,k):
    if(prime(a+n+g)):
        print(g)
        break
    else:
        g=g+1
    