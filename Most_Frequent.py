n=int(input())
l=list(map(int,input().split()))
t=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c>t:
        t=c
        ti=l[i]
    if c==t:
        if ti>l[i]:
            ti=l[i]
print(ti)