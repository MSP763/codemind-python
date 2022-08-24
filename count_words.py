x=input()
c=0
a="aeiouAEIOU"
b="qwrtypsdfghjklzxcvbnmQWRTYPASDFGHJKLZXCVBNM"
for i in x.split():
    d=len(i)
    if i[0] in a:
        if i[d-1] in b:
            c+=1
print(c)