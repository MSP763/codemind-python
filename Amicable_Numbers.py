a=int(input())
b=int(input())
sum=0
sum1=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
for i in range(1,b):
    if b%i==0:
        sum1=sum1+i
if sum1==a and sum==b:
    print("Amicable")
else:
    print("Not Amicable")
    