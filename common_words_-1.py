x=input().lower().split()
y=input().lower().split()
a=[]
for i in x:
    if i in y:
        a.append(i)
print(len(a))