s=input()
l=list(s)
i=0
j=len(s)-1
while i<j:
    if not l[i].isalpha():
        i=i+1
    elif not l[j].isalpha():
        j=j-1
    else:
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1
k="".join(l)
print(k)
    