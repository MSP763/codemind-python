n=int(input())
l=list(map(int,input().split()))
m=int(input())
ll=list(map(int,input().split()))
l=sorted(l)
ll=sorted(ll)
if m==n:
    c=0
    for i in range(n):
        if l[i]!=ll[i]:
            c=1
            break
    if c==1:
        print("False")
    else:
        print("True")
else:
    print("False")