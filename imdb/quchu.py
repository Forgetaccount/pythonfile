f2=open('imdb_prodco_node_num_n.txt','r')
f1=open('imdb_prodco_class.txt','r')
f3=open('imdb_wuguli.txt','w')
f4=open('imdb_wuguliclass.txt','w')
key={}
for line in f2.readlines():
    line = line.strip()
    s = line.split()
    #print(s[1])
    if float(s[1])==0:
        print(s[1])
        continue
    else:
        key[s[0]]=1
        f3.write(line+"\n")
f2.close()
for line in f1.readlines():
    line = line.strip()
    s = line.split()
    if s[0] in key:
        f4.write(line+"\n")
    else:
        continue

