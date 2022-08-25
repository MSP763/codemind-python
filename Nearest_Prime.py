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
for i in range(n):
    a=int(input())
    for j in range(a,1,-1):
        if(prime(j)):
            k=j
            break
    l=a+1
    while(1):
        if(prime(l)):
            m=l
            break
        l=l+1 
    b=abs(a-k)
    c=abs(a-m)
    if(b>c):
        print(m)
    else:
        print(k)