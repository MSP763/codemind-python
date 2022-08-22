a=input()
b=[]
c=[]
for i in a:
    if i.isalnum():
        b.append(i)
b=sorted(b)
j=0
for i in a:
    if i.isalnum():
        print(b[j],end="")
        j+=1
    else:
        print(i,end="")