a=input("")
a=a.lower()
tool=len(a)
i=0
while i<tool:
    if a[i]=="e":
        a=a[:i]+a[i+1:]
        i=i-1
        tool=tool-1
    if a[i]=="a":
        a=a[:i]+a[i+1:]
        i=i-1
        tool=tool-1
    if a[i]=="u":
        a=a[:i]+a[i+1:]
        i=i-1
        tool=tool-1
    if a[i]=="o":
        a=a[:i]+a[i+1:]
        i=i-1
        tool=tool-1
    if a[i]=="i":
        a=a[:i]+a[i+1:]
        i=i-1
        tool=tool-1
    i=i+1
    
t=0
tool=len(a)
while t<tool:
    a=a[:t]+"."+a[t:]
    t=t+2
    tool=len(a)
print(a)







