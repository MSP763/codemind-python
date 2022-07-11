n=int(input())
for i in range(n):
    k=int(input())
    arr=list(map(int,input().strip().split()))
    if(sorted(arr)==arr):
        print("0")
    else:
        arr.sort()
        print(abs(max(arr)-min(arr)))
    
    