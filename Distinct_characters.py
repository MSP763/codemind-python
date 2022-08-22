s=input().lower().replace(" ","")
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a=sorted(a)
for i in a:
    print(i,end="")