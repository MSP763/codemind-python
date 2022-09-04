n=int(input())
t=c=0
l=list(map(int,input().split()))
for i in range(n):
    if l[i]==1:
        c+=1
    if l[i]!=1:
        if c>t:
            t=c
        c=0
if c>t:
    t=c
print(t)