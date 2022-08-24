x=input()
ch=input()
n,d=0,0
for i in x:
    if(ch==i):
        print('True')
        print(d)
        n=1
        break
    d+=1
if(n==0):
    print('False')