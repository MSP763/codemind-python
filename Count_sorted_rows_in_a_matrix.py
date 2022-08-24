x,y=map(int,input().split())
c=0
for i in range(x):
    a=list(map(int,input().split()))
    if(a==sorted(a)or a==sorted(a)[::-1]):
        c+=1
print(c)