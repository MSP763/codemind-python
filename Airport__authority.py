x=int(input())
a=[]
for i in range(0,x):
    n=int(input())
    a.append(n)
y=int(input())
sum=0
for i in range(0,x):
    if a[i]>y:
        sum+=2
    else:
        sum+=1
print(sum)