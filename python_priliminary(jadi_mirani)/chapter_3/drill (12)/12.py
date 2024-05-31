motarjem=dict()
tool=int(input(""))
i=0
while i<tool:
    my_string=input("")
    my_list=my_string.strip().split()
    yek=my_list[0]
    do=my_list[1]
    motarjem[yek]=do
    i=i+1
my_sentences=input("")
my_list=my_sentences.strip().split()
tool=len(my_list)
i=0
jomle=[]
while i<tool:
    t=my_list[i]
    if t in motarjem.keys():
        e=11
    else:
        motarjem[t]=t
    jomle=jomle+[motarjem[t]]
    i=i+1
nahai=" ".join(jomle)
print(nahai)