n,k=map(int,input().split())
l=list(map(int,input().split()))[:n]
c=0
for i in l:
    if i%k==0:
        c+=1
print(c)