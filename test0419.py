'''f1=open('pr-weight.txt','r')
f2=open('pr_w2.txt','w')
node_w={}
for line in f1.readlines():
    line=line.strip()
    s=line.split(",")
    str=s[0]+","+s[1]
    str1=s[1]+","+s[0]
    if str in node_w:
        continue
    if str1 in node_w:
        continue
    node_w[str]=s[2]
    f2.write(line+"\n")
'''



f=open('imdb_prodco_class.txt','r')#1
f1=open('imdb_w2.txt','r')
node_c={}#node---asso
for line in f.readlines():
    line=line.strip()
    s=line.split()
    node_c[s[0]]=s[1]

f.close()
w=open('imdb_cs.txt','w')
#w1=open("imdb_cs1.txt",'w')
for line in f1.readlines():
    line=line.strip()
    s=line.split(",")
    attr=node_c[s[0]]
    wri=str(s[0])+"\t"+str(s[1])+"\t"+str(s[2])+"\t"+attr+"\t"+node_c[s[1]]+"\n"
    w.write(wri)


