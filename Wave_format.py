n=input()
l=list(map(int,input().split()))
a,b=[],[]
while(len(l)>0):
    b.append(max(l))
    l.remove(max(l))
    if(len(l)==0):
        break
    a.append(max(l))
    l.remove(max(l))
m=min(len(a),len(b))
ma=max(len(a),len(b))
for i in range(m):
    print(a[i],end=' ')
    print(b[i],end=' ')
if len(b)>len(a):
    for i in range(m,ma):
        print(b[i],end=' ')