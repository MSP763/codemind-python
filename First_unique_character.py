s=input().lower().replace(" ","")
a=0
for i in s:
    if s.count(i)==1:
        print(i)
        a=1
        break
if(a==0):
    print('-1')