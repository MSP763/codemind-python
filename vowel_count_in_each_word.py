a=input().lower().split()
ch='aeiou'
b=[]
for i in a:
    j=str(i)
    c=0
    for k in j:
        if(k in ch):
            c+=1
    print(c,end=" ")