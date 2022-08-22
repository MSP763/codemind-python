b=input()
a=[]
for i in b:
    if(i!=' '):
        a.append(i)
print(min(a),a.count(min(a)),max(a),a.count(max(a)))