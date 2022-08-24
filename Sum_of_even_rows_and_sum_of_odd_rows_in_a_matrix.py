a,b=map(int,input().split())
c1,c2=0,0
for i in range(a):
    c=list(map(int,input().split()))
    if(i%2==0):
        c1+=sum(c)
    else:
        c2+=sum(c)
print(c1,c2)