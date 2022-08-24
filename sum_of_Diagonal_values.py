m,n=map(int,input().split())
s1=[list(map(int,input().split())) for i in range(m)]
c=0
for i in range(m):
    for j in range(n):
        if(i==j):
            c+=s1[i][j]
        elif(i==n-j-1):
            c+=s1[i][j]
print(c)