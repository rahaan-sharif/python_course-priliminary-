a=input("")
tool=len(a)
i=0
aval=0
aval_A=0
dovom=0
aval_B=0
while i<tool :
    if a[i]=="A":
        if i+1<tool:
            if a[i+1]=="B":
                aval=1
                aval_A=1
                i=i+1
                break
    if a[i]=="B":
        if i+1<tool:
            if a[i+1]=="A":
                aval=1
                aval_B=1
                i=i+1
                break
    i=i+1
while i<tool :
    if a[i]=="A":
        if i+1<tool:
            if aval_B==1:
                if a[i+1]=="B":
                    dovom=1
                    break
    if a[i]=="B":
        if i+1<tool:
            if aval_A==1:
                if a[i+1]=="B":
                    dovom=1
                    break
    i=i+1
if aval==1:
    if dovom==1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
