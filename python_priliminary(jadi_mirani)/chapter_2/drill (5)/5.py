a=0
max=0
do_max=0
while a!=-1:
    a=int(input(""))
    if a>do_max:
        do_max=a
    if a>max:
        do_max=max
        max=a
#if a>max:
#       do_max=max
#       max=a
print(max,do_max)