a,b,c=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
    t=l[a-1]
    for j in range(a-1,0,-1):
        l[j]=l[j-1]
    l[0]=t
for i in range(c):
    v=int(input())
    print(l[v])