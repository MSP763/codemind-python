n=int(input())
l=list(map(int,input().split()))
t=0
for i in range(1,max(l)+1):
    c=0
    for j in range(n):
        if i==l[j]:
            c=1
    if c==0:
        if i>0:
            print(i)
            t=1
            break
if t==0:
    print(max(l)+1)