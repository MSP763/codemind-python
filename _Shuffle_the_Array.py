n=int(input())
l=list(map(int,input().split()))
for i in range(n//2):
    print(l[i],end=' ')
    print(l[n//2+i],end=' ')