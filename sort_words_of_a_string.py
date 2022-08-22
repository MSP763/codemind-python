x=input().split()
a=[]
for i in x:
    j=str(i)
    c=[]
    d=''
    for k in j:
        if(k.isalnum()):
            c.append(k)
    c=sorted(c)
    m=0
    for k in j:
        if(k.isalnum()):
            d+=c[m]
            m+=1
        else:
            d+=k
    a.append(d)
print(*a)