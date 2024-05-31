a=input("")
natije=""
tool=len(a)
i=0
while i<tool:
    if a[i]=="h":
        n=len(natije)
        natije=natije[:n]+"h"
        i=i+1
        break
    i=i+1
while i<tool:
    if a[i]=="e":
        n=len(natije)
        natije=natije[:n]+"e"
        i=i+1
        break
    i=i+1
while i<tool:
    if a[i]=="l":
        n=len(natije)
        natije=natije[:n]+"l"
        i=i+1
        break
    i=i+1
while i<tool:
    if a[i]=="l":
        n=len(natije)
        natije=natije[:n]+"l"
        i=i+1
        break
    i=i+1
while i<tool:
    if a[i]=="o":
        n=len(natije)
        natije=natije[:n]+"o"
        i=i+1
        break
    i=i+1
if natije=="hello":
    print("YES")
else:
    print("NO")