x=int(input())
b=[]
i=0
c=0
while x>0:
    r=x%10
    c=c+1
    b.append(r)
    x=x//10
d=0
k=0
for i in range(c):
    for j in range(c):
        if b[i]==b[j] and i!=j:
            print('Not Unique Number')
            k=1
            break
    if k==1:
        break
    else:
        d=d+1
if c==d:
    print('Unique Number')