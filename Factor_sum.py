l=list(map(int,input().split(',')))
p=0
for i in set(l):
    s=0
    t=0
    for j in range(1,i+1):
        if i%j==0:
            t+=j
    for k in l:
        if t==k:
            s=1
    if s==1:
        print(i,end=' ')
        p=1
if p==0:
    print(-1)