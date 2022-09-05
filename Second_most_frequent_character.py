s=input()
c=[]
for i in s:
    c.append(s.count(i))
m=max(set(c))
c=set(c)
c.remove(m)
d=[]
for i in s:
    if s.count(i) in c:
        print(i)
        break
if len(c)==0:
    print("-1")












    