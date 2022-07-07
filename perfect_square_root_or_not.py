x=int(input())
import math
s=math.sqrt(x)
y=(s-math.floor(s))
if y==0:
    print("True")
else:
    print("False")