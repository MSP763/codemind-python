l=int(input())
n=int(input())
while(n>0):
    n-=1
    w,h=map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
        
    else:
        if w==h:
            print("ACCEPTED")
           
        else:
            print("CROP IT")