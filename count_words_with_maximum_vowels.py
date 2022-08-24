x=input().split()
ch='aeuioAEUIO'
c=0
d=[]
for i in x:
    j=str(i)
    c=0
    for k in j:
        if k in ch:
            c+=1
    d.append(c)
g=max(d)
print(d.count(g))