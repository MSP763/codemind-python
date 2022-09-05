def prime(n):
    prime=True
    if n==2:
        return 1
    else:
        for i in range(2,n):
            if n%i==0:
                prime=False
    if prime:
        return 1
    else:
        return 0
x=int(input())
if prime(x):
    print("prime")
else:
  print("not a prime")  