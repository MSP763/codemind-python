def pal(n):
    temp=n
    s=0
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==temp):
        return 1
    else:
        return 0
n=int(input())
for i in range(1,n):
    if(pal(i)):
        k=i
i=n+1
while(1):
    if(pal(i)):
        m=i
        break
    i=i+1
if(abs(n-k)>abs(n-m)):
    print(m)
elif(abs(n-k)==abs(n-m)):
    print(k,m)
else:
    print(k)