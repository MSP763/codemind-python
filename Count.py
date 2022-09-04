n=int(input())
ar=[]
e,o=0,0
s=list(map(int,input().strip().split()))
for i in range(n):
    ar.append(s[i])
for i in range(n):
    if ar[i]%2==0:
        e+=1
    else:
        o+=1
print("%d %d"%(e,o))