tool=int(input(""))
i=0
quality=[]
price=[]
laptop=""
while i<tool :
    laptop=input("")
    my_list=laptop.strip().split()
    
    my_list[1]=int(my_list[1])
    my_list[0]=int(my_list[0])
    price=price+[my_list[0]]
    quality=quality+[my_list[1]]
    i=i+1

i=0
j=0
s=0
while i<tool :
    j=0
    while j<i:
        if price[j]<price[i]:
            if quality[j]>quality[i]:
                s=1
                 
        if price[j]>price[i]:
            if quality[j]<quality[i]:
                s=1
                
        j=j+1
    i=i+1

i=0
j=0

if s==0:
    print("poor irsa")
else:
    print("happy irsa")






