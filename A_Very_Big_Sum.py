n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    s+=l[i]
print(s)