n=int(input())
l1=list(map(int,input().strip().split()))
l2=list(map(int,input().strip().split()))
for i in range(n):
    print(l1[i]+l2[i],end=' ')