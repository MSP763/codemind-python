x=int(input())
a=list(str(x))
for i in range(len(a)):
    if(a[i]=='6'):
        a[i]='9'
        break
    else:
        continue
a=''.join(a)
print(int(a))