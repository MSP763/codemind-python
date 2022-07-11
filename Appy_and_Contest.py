t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    c=n//a
    c1=n//b
    c2=n//(a*b)
    if(c+c1-c2>=k):
        print("Win")
    else:
        print("Lose")