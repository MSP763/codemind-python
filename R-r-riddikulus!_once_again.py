a,b=map(int,input().split())
arr=list(map(int,input().split()))
print(*arr[b:]+arr[:b])