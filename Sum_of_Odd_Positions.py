x=int(input())
a=list(map(int,input().split()))
s1=0
for i in range(x):
    if(i%2!=0):
        s1+=a[i]
print(s1)