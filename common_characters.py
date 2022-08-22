s1=input().lower()
s2=input().lower()
a=[]
c=0
for i in s1:
    if i in s2 and i!=' ':
        a.append(i)
        c=1
a=sorted(set(a))
if(c==0):
    print('-1')
else:
    for i in a:
        print(i,end="")