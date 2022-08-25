def ab(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    return s
n=int(input())
if(ab(n)>n):
    print("True")
else:
    print("False")