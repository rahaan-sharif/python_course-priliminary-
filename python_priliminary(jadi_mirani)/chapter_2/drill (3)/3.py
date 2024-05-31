count=0
bord=0
jam=0
while count<30:
    a=int(input(""))
    count=count+1
    jam=jam+a
    if a==3:
        bord=bord+1
print(jam ,bord)
