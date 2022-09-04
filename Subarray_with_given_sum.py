nt=int(input())
for p in range(nt):
    n,b=map(int,input().split())
    a=list(map(int,input().split()))
    s,t=0,0
    for i in range(n):
        c=0
        for j in range(i,n):
            c+=a[j]
            if c==b:
                print(i+1,j+1)
                s=1
                break
        if s==1:
            t=1
            break
    if t==0:
        print(-1)