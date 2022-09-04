n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    max=0
    for j in range(i+1,n):
        if l[j]>max:
            max=l[j]
        l[i]=max
l[n-1]=-1
print(*l)