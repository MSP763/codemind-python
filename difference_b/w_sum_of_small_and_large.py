s=input().split()
maxi=[]
mini=[]
smax=0
smin=0
for i in s:
    maxi.append(ord(max(i)))
    mini.append(ord(min(i)))
for j in maxi:
    smax+=int(j)
for j in mini:
    smin+=int(j)
print(abs(smax-smin))