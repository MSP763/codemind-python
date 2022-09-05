s=input()
c=0
r=0
for i in range(0,len(s)):
    if s[i] in "aeiou":
        c=c+1
    else:
        r=max(r,c)
        c=0
print(max(c,r))        
        