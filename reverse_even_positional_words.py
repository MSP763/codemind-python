x=input().split()
n=0
for i in x:
    if(n%2==0):
        print(i[::-1],end=" ")
    else:
        print(i,end=" ")
    n=n+1