r=int(input())
c=int(input())
s=0
for i in range(r):
    arr=list(map(int,input().strip().split()))
    for j in arr:
        s=s+j
print(s)        