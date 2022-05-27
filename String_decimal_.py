x=int(input())
for i in range(x):
    y=input()
    c=0
    l=len(y)
    for char in y:
        if char.isdigit():
            c+=1
    if(c==l):
        print('True',end='
')
    else:
        print("False",end='
')