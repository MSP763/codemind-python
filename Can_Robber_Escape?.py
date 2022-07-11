n=int(input())
arr=list(map(int,input().strip().split()))
c=0
for i in range(n):
    if(arr[i]%2!=0):
        c=c+1
if(c<=2):
    print("YES")
else:
    print("NO")