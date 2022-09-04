n=int(input())
t=2
l=list(map(int,input().split()))
l.sort(reverse=True)
for i in range(1,n):
    if l[i]<l[i-1]:
        t-=1
    if t==0:
        print(l[i])
        break
else:
    print(l[0])