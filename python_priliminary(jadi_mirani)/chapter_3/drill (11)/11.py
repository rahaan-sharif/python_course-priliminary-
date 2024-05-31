tool=int(input(""))
i=0
ashkhas=dict()
while i<tool :
    w=input("")
    if w in ashkhas:
        ashkhas[w]=ashkhas[w]+1
    else:
        ashkhas[w]=1
    i=i+1
  
#-------------------------------
my_list=list(ashkhas.keys())
tool=len(my_list)
i=0
while i<tool:
    w=min(my_list)
    print(w ,ashkhas[w])
    my_list.remove(w)
    i=i+1


