t=int(input())
for i in range(t):
    c=0
    a,b=map(int,input().split())
    for j in range(b):
        if (j*j)%b==a:
            print(j)
            c+=1
            break
    if c==0:
        print("-1")