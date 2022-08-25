n=int(input())
s=0
fact=1
temp=n
while(n):
    i=1
    fact=1
    d=n%10
    while(i<=d):
        fact=fact*i
        i=i+1
    s=s+fact
    n=n//10
if(s==temp):
    print("The number %d is a strong number"%temp)
else:
    print("The number %d is not a strong number"%temp)
    