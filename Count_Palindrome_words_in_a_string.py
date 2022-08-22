x=input()
x=x.lower().split()
c=0
for i in x:
    if(i==i[::-1]):
        c+=1
print(c)