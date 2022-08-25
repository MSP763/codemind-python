n=int(input())
sq=n*n
sum=0
sum1=0
while n!=0:
    r=n%10
    sum=sum*10+r
    n=n//10
sq1=sum*sum
while sq1!=0:
    r=sq1%10
    sum1=sum1*10+r
    sq1=sq1//10
if sum1==sq:
    print("True")
else:
    print("False")