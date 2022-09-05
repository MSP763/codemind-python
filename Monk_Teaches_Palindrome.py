n=int(input())
for i in range(n):
    s=input()
    d=s[::-1]
    if s==d:
        print("YES",end=' ')
        if len(s)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")