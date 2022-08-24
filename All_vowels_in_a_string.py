a=input()
ch1='aeuio'
ch2='AEUIO'
c=[]
d=[]
for i in a:
    if i in ch1:
        c.append(i)
for i in a:
    if i in ch2:
        d.append(i)
c1=len(list(set(c)))
c2=len(list(set(d)))
if(c1==5 or c2==5):
    print('True')
else:
    print('False')