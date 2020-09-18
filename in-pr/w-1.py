

f=open('industry-pr.rn','r')#1
w=open('pr-weight.txt','w')#1
weight={}
k=0
for line in f.readlines():
    line=line.strip()
    s=line.split(",")
    pinjie=s[0]+","+s[1]

    pj=s[1]+","+s[0]
    #print(weight)
    if ( pj in weight.keys()) |(pinjie in weight.keys()) :
        k=k+1
    else:
        w.write(line+"\n")

    weight[pinjie] = s[2]
print(k)
f.close()
w.close()


