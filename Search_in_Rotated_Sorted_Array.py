def search(n,l,s):
    for i in range(n):
        if l[i]==s:
            return i
    return -1
n=int(input())
l=list(map(int,input().strip().split()))
s=int(input())
print(search(n,l,s))