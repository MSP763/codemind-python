n=input()
s=''
for i in n:
    if i=='0':
        continue
    elif int(i)%2==0:
        continue
    else:
        sqr=int(i)**2
        s=s+str(sqr)
print(s)        