x=input().split()
a=[]
for i in x:
    a.append(min(i))
    a.append(max(i))
print(*a)