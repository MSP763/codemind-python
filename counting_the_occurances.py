n=input()
m=input()
c=0
for i in n:
    if i==m[0]:
        c+=1
if c==0:
    print("-1")
else:
    print(c)
    