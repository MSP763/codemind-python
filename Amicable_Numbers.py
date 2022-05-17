x=int(input())
y=int(input())
sum=0
sum2=0
i=1
for i in range(1,(x//2)+1):
    if x%i==0:
        sum+=i
for i in range(1,(y//2)+1):
    if y%i==0:
        sum2+=i
if x==sum2 and y==sum:
    print('Amicable')
else:
    print('Not Amicable')