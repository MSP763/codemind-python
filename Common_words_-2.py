a=input().split()
b=input().split()
c=0
d=[]
for i in a:
    if(i in b):
        d.append(i)
for i in d:
    if(a.count(i)==1 and b.count(i)==1):
        c+=1
print(c)