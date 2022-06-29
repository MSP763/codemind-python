x=int(input())
a=list(map(int,input().split()))
s1,s2=0,0
for i in range(x):
    if(a[i]%2==0):
        s1+=a[i]
    else:
        s2+=a[i]
print(abs(s1-s2))