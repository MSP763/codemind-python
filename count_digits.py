n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if(i<0):
        i=-i
    j=len(str(i))
    b.append(j)
print(*b)