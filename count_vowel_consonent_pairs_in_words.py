a=input().split()
ch='aeuioAEUIO'
ch2='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
c=0
for i in a:
    j=str(i)
    d=len(j)-1
    for k in range(len(j)//2):
        if(j[k] in ch and j[d] in ch2):
            c+=1
        elif(j[k] in ch2 and j[d] in ch):
            c+=1
        d=d-1
print(c)