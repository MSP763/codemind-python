a,b=map(int,input().split())
s=[list(map(int,input().split()))for i in range(a)]
c=0
for j in range(b):
    d=[]
    for i in range(a):
        d.append(s[i][j])
    if(d==sorted(d) or d[::-1]==sorted(d)):
        c+=1
print(c)