x=int(input())
c=0
for i in range(1,x):
    if x==i*(i+1):
        print('YES')
    else:
        c=c+1;
if c==x-1:
    print('NO')