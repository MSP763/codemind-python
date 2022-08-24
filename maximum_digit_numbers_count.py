n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    j=str(i)
    d.append(len(j))
s=max(d)
for i in a:
    j=str(i)
    if(s==len(j)):
        print(i,end=" ")