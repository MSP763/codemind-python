n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==1:
        s.append(l[i])
if len(s)>0:
    print(*s)
else:
    print("-1")