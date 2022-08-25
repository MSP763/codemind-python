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
f=0
for i in range(1,n+1):
    if(prime(i)):
        for j in range(1,n+1):
            if(prime(j)):
                if(i*j==n):
                    f=1
                    l=i
                    g=j
if(f==0):
    print("-1")
else:
    print(g,l)