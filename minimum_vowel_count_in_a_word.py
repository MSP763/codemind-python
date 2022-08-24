x=input().lower().split()
ch='aeuio'
a=[]
for i in x:
    j=str(i)
    c=0
    for k in j:
        if(k in ch):
            c+=1
    a.append(c)
print(min(a))