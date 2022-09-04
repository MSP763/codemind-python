a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
for i in range(len(a)):
    if(a[i]>b[i]):
        c=c+1
    elif(a[i]==b[i]):
        continue
    elif(a[i]<b[i]):
        d=d+1
            
print(c,d)            