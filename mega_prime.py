n=int(input())
fact=0
dig=0
pr=0
for i in range(1,n+1):
    if n%i==0:
        fact+=1
if fact==2:
    while n>0:
        fact=0
        m=n%10
        for j in range(1,m+1):
            if m%j==0:
                fact+=1
        if fact==2:
            pr+=1
        dig+=1
        n=n//10
    if dig==pr:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")