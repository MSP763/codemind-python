x=int(input())
c=0
a=list(map(int,input().split()))
for i in range(0,x):
    for j in range(0,x):
        if a[i]==a[j]and i!=j:
            print(a[i])
            c=1
    if c==1:
        break