x=int(input())
a=[]
while(x>0):
    r=x%10
    a.append(r)
    x=x//10
for i in range(len(a)-1,-1,-1):
    if a[i]==6:
        a[i]=9
        break
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")