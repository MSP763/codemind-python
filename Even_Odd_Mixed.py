n=int(input())
s=0
o=0
e=0
while n!=0:
    r=n%10
    s+=1
    if r%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if e==s:
    print("Even")
elif o==s:
    print("Odd")
else:
    print("Mixed")