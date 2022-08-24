a=input()
ch='aeuioAEUIO'
c=0
d=[]
for i in a:
    if i in ch:
        if(i not in d):
            d.append(i)
            c=1
if(c==0):
    print('-1')
else:
    print(*d)