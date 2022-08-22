x=input().split()
for i in x:
    print(ord(max(i))-ord(min(i)),end=" ")