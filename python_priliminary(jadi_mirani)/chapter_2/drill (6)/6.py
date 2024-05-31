def bishtarin(a):
    count=0
    i=1
    while i<=a:
        if a%i==0:
            count=count+1
        i=i+1
    return count
i=0
max=1
while i<20:
    a=int(input(""))
    i=i+1
    if bishtarin(a)>bishtarin(max):
        max=a
    if bishtarin(a)==bishtarin(max):
        if a>max:
            max=a
print(max,bishtarin(max))