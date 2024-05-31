tedad=int(input(""))
i=0
shoraka=input("")
sharikan=shoraka.strip().split()
while i<tedad:
    sharikan[i]=int(sharikan[i])
    i=i+1
i=0
shomare=0
while i<tedad:
    if sharikan[i]<=2:
        shomare=shomare+1
    i=i+1
print(int(shomare/3))