n=int(input())
for i in range(n):
    k=int(input())
    s=input()
    l=[]
    for i in s:
        if(s.count(i)==1):
            l.append(i)
    for j in range(0,len(l)):
        print(l[j])
        break
    if(len(l)==0):
        print("-1")