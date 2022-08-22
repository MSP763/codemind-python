x=input().lower().split()
a=list(str(x[0]))
c=0
for i in a:
    c1=0
    for j in range(1,len(x)):
        k=list(str(x[j]))
        if i in k:
            c1+=1
    if(c1==len(x)-1):
        c+=1
print(c)