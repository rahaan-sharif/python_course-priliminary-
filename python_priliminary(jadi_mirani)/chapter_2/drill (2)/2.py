a=int(input(""))
b=2
c=0
while b<a:
    if a%b==0:
        c=1
        break
    b=b+1
if c==0:
    print("prime")
if c==1:
    print("not prime")
