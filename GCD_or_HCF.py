a,b=map(int,input().split())
i=0
if a>b:
    for t in range(2,a+1):
        if a%t==0 and b%t==0:
            i=t
    if i!=0:
        print(i)
    else:
        print("1")
else:
    for t in range(2,b+1):
        if a%t==0 and b%t==0:
            i=t
    if i!=0:
        print(i)
    else:
        print("1")