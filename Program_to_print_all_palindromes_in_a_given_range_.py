a=int(input())
b=int(input())
for i in range(a,b+1):
    s=0
    k=i
    while(i):
        d=i%10
        s=s*10+d
        i=i//10
    if(s==k):
        print(s,end=' ')