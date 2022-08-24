n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    j=len(str(i))
    b.append(j)
m=max(b)
c=b.count(m)
print(c)