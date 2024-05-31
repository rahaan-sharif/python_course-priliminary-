a=input("")
tool=len(a)
natije=""
i=0
tool=len(a)
while i<tool:
    if a[i]=="1":
        natije=natije[:len(natije)]+a[i]
    i=i+1
i=0
while i<tool:
    if a[i]=="2":
        natije=natije[:len(natije)]+a[i]
    i=i+1
i=0
while i<tool:
    if a[i]=="3":
        natije=natije[:len(natije)]+a[i]
    i=i+1
i=1
tool=len(natije)
while i<tool:
    natije=natije[:i]+"+"+natije[i:]
    i=i+2
    tool=len(natije)
print(natije)