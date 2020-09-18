
f1=open('node_class.txt','r')#2
node_c={}#node---class
for l in f1.readlines():
    line=l.strip()
    s=line.split()
    node_c[s[0]]=s[1]
f=open('node_num_n.txt','r')#1
node_num={}#node---num
node_n={}#node---asso
class_cl=['Technology','Healthcare','Financial','Energy','BasicMaterials',
          'CapitalGoods','Utilities','ConsumerNonCyclical','Transportation',
          'Conglomerates','ConsumerCyclical','Services']
for line in f.readlines():
    line=line.strip()
    s=line.split()
    x=s[0]
    pinjie=s
    node_num[s[0]]=s[1]
    del(pinjie[0])
    del(pinjie[0])
    node_n[x]=pinjie
f.close()
last={}

for a in node_n:
    asso=node_n[a]
    list = []
    bbb = ""
    for aaa in asso:
        for d in node_n[a]:
            if d==a:
                continue
            if d in list:
                continue
            list.append(d)
            bbb = bbb + d + " "
        b = node_n[aaa]
        for bb in b:
            if bb==a:
                continue
            if bb in list:
                continue
            list.append(bb)
            bbb = bbb + bb + " "
    last[a] = str(bbb)


ff=open('aaaaadxx.txt','w')
for cc in last:
    l1=last[cc].split(" ")
    l2=len(l1)-1
    ff.write(str(cc)+" "+str(l2)+" "+str(last[cc])+"\n")



