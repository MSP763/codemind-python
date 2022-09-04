n=int(input())
arr=list(map(str,input().strip().split()))
b=""
for i in arr:
    b+=i
print(*list(str(int(b)+1)))    