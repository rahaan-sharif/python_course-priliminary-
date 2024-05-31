import math
tedad=int(input(""))
group=[]
i=0
while i<tedad :
    w=int(input(""))
    group=group+[w]
    i=i+1
i=0
j=0


while i<tedad :
    w=int(10000*math.sqrt(group[i]))
    w_0=w//10000
    w=w%10000######
    w_1=w//1000
    w=w%1000########
    w_2=w//100
    w=w%100#######
    w_3=w//10
    w_4=w%10
    naha=(w_0)+(w_1/10)+(w_2/100)+(w_3/1000)+(w_4/10000)
    
    
    
    ae="{:.4f}"
    c=ae.format(naha)
    print(c)
    i=i+1

