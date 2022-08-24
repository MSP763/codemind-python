a=input()
ch='aeiou'
d=0
for i in ch:
    if i not in a:
        print(i,end=" ")
        d=1
if(d==0):
    print('0')