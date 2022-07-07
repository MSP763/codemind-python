n=int(input())
f=0
c=0
s=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    m=n
    while m!=0:
        r=m%10
        s=s*10+r
        m=m//10
    for j in range(1,s+1):
        if s%j==0:
            c+=1
    if c==2:
        print('circular prime')
    else:
        print("prime but not a circular prime")
else:
    print("not prime")