m,n=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    j=str(i)
    if(j[0]=='-'):
        if(n==len(j)-1):
            c+=1
    elif(n==len(j)):
        c+=1
print(c)