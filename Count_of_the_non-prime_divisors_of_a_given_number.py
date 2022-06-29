x=int(input())
s=0
for i in range(1,x+1):
    c=0
    if(x%i==0):
        for j in range(1,i+1):
            if(i%j==0):
                c+=1
        if(c!=2):
            s+=1
print(s)