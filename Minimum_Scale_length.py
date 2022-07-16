n=int(input())
arr=list(map(int,input().strip().split()))
m=max(arr)
for i in range(m,0,-1):
    c=0
    for j in range(n):
        if(arr[j]%i==0):
            c=c+1
    if(c==n):
        print(i)
        break
    
    