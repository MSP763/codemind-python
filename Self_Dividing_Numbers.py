n=int(input())
m=int(input())
for i in range(n,m+1):
    l=i
    s=i
    c=0
    f=0
    while l!=0:
        r=l%10
        c+=1
        if r==0:
            break
        if s%r==0:
            f+=1
        l=l//10
    if f==c:
        print(i,end=' ')