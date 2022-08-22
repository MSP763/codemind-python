s=input().lower().replace(" ","")
s=sorted(list(set(s)))
for i in s:
    print(i,end="")