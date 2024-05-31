esm=input("")
bozorg=0
koochik=0
tool=len(esm)
i=0
while i<tool :
    if esm[i]==esm[i].upper():
        bozorg=bozorg+1
    i=i+1
i=0
while i<tool :
    if esm[i]==esm[i].lower():
        koochik=koochik+1
    i=i+1
if koochik<bozorg:
    print(esm.upper())
else:
    print(esm.lower())
