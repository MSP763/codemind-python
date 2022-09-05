n=int(input())
x=0
for i in range(n):
    s=input()
    if(s[0]=="+" or s[2]=="+"):
        x=x+1
    elif(s[0]=="-" or s[2]=="-"):
        x=x-1
print(x)    
    