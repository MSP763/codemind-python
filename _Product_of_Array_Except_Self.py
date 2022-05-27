x=int(input())
a=list(map(int,input().split()))
for i in range(0,x):
    f=1
    for j in range(0,x):
        if i!=j:
            f=f*a[j]
    print(f,end=" ")