x=input()
c=0
for i in x:
    if(i.isalpha() or i.isdigit()):
        continue
    if(i==' '):
        continue
    c+=1
print(c)