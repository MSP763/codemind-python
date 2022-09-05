str = input() 
sd=0
for x in str:
    if x.isdigit():
        sd = sd+ int(x)

print(sd)