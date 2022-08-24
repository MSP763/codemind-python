a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
s=0
k=len(d)
d=list(set(d))
for i in d:
    if(i in c):
        s+=1
if(s==k):
    print('Yes')
else:
    print('No')