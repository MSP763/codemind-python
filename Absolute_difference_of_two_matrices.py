n=int(input())
s1=[list(map(int,input().split())) for i in range(n)]
s2=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n-1):
        print(abs(s1[i][j]-s2[i][j]),end=" ")
    print(abs(s1[i][j+1]-s2[i][j+1]),end='')
    print()