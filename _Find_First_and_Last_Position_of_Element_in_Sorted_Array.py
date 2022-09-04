n=int(input())
l=list(map(int,input().strip().split()))
s=int(input())
c=0
for i in range(n):
    if l[i]==s:
        print(i,end=' ')
        c+=1
        break
for i in range(n-1,-1,-1):
    if l[i]==s:
        print(i,end=' ')
        break
if c==0:
    print('-1 -1')