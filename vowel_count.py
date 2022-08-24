a=input()
ch='aeiouAEIOU'
c=0
for i in a:
    if i in ch:
        c+=1
print(c)