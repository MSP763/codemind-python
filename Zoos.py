
s=input()
c=0
c1=0
for char in s:
    if char=='z':
        c+=1
    if char=='o':
        c1+=1
if c1==2*c:
    print('Yes')
else:
    print('No')