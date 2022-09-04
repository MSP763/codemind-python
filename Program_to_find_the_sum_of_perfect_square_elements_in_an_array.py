import math
n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(len(arr)):
    k=math.sqrt(arr[i])
    if(int(k+0.5)**2==arr[i]):
        s=s+arr[i]
print(s)        