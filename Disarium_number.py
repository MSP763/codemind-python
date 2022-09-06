a=int(input())
u=t=a
i=0
s=0
while a!=0:
    j=a%10
    a=a//10
    i=i+1
j=0
for i in range(i,0,-1):
    j=u%10
    s+=pow(j,i)
    u=u//10
if s==t:
    print("True")
else:
    print("False")