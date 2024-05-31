a=input("")
my_list=a.strip().split()
i=0
tool=len(my_list)
while i<tool:
    my_list[i]=int(my_list[i])
    i=i+1

ma=max(my_list)
mi=min(my_list)
javab=ma-mi
if javab%1!=0:
    print(int(javab))
else:
    print(javab)
