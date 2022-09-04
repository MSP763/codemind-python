n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(i,n):
        if l[j]>l[i]:
            c=1
            break
    if(j-i==0 or c==0):
        print(0,end=' ')
    else:
        print(j-i,end=' ')