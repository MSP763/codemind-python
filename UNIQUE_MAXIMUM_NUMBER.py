n=int(input())
l=list(map(int,input().split()))
max=0
m=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==1:
        if l[i]>max:
            max=l[i]
            m+=1
if m==0:
    print("-1")
else:
    print(max)