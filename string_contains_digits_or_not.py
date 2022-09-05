n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in s:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8'  or i=='9':
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")