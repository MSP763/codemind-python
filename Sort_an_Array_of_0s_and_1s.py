x=int(input())
a=list(map(int,input().split()))
d=sorted(a)
for i in range(x):
     print(d[i],end=" ")