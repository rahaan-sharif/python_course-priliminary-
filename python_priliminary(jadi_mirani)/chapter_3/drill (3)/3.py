def asami(esm):
    tool=len(esm)
    a=esm[0]
    esm=esm[1:]
    a=a.upper()
    esm=esm.lower()
    esm=a+esm
    return esm
i=0
voroodi=["","","","","","","","","",""]
while i<10:
    voroodi[i]=input("")
    voroodi[i]=asami(voroodi[i])
    i=i+1
i=0
while(i<10):
    print(voroodi[i])
    i=i+1