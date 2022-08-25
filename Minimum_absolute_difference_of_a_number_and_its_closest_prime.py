def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
if(prime(n)):
    print("0")
    exit()
for i in range(1,n):
    if(prime(i)):
        k=i
i=n+1
while(1):
    if(prime(i)):
        m=i
        break
    i+=1
if(abs(k-n)>abs(m-n)):
    print(abs(n-m))
elif(abs(k-n)==abs(m-n)):
    print(abs(k-n))
else:
    print(abs(n-k))