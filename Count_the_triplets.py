t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    f=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j] in arr):
                c=c+1
                f=1
    if(f==0):
        print("-1")
    else:    
        print(c)