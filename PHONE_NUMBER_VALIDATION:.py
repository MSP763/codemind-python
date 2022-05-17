x=int(input())
r=0
c=0
while x>0:
    r=x%10
    c=c+1
    x=x//10
if c<9 or r==0 or c>10:
    print('Invalid')
else:
    print('Valid')