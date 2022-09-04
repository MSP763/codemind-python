a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=0
d=0
for i in range(a):
    if(arr[i]<=b):
        c=c+1
    elif(arr[i]>b):
        d=d+1
        if(d==2):
            break
print(c)        
    