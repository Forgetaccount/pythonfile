import numpy as np
from sklearn.model_selection import train_test_split
import math
f=open('node_num_n.txt','r')#1
node_num={}#node---num
node_n={}#node---asso
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

f1=open('node_class.txt','r')#2
node_c={}#node---class
c_num={}#node-----num0--2188
num_c={}#所有数字对应node  num0-2188----node
ll=0
for l in f1.readlines():
    line=l.strip()
    s=line.split()
    node_c[s[0]]=s[1]
    c_num[s[0]]=ll
    num_c[ll] = s[0]
    ll=ll+1

class_cl=['Technology','Healthcare','Financial','Energy','BasicMaterials',
          'CapitalGoods','Utilities','ConsumerNonCyclical','Transportation',
          'Conglomerates','ConsumerCyclical','Services']


weight={}
ff=open('pr-weight.txt','r')#2
for line in ff.readlines():
    line=line.strip()
    s=line.split(",")
    pinjie=s[0]+","+s[1]
    weight[pinjie] = s[2]

jj = 0
zl = 0
sum = 0
accu = 0

for jj in range(1):
    v4 = open('v4.txt', 'w')
    v5 = open('v5.txt', 'w')
    v6 = open('v6.txt', 'w')
    v7 = open('v7.txt', 'w')
    tw = {}
    vw = {}
    print(jj)
    wvrn = {}
    train_data = []
    valid_data = []
    # 每个类按比例抽取
    my_matrix = np.loadtxt(open("node_class.txt"), dtype=str, skiprows=0)
    X, y = my_matrix[:, :-1], my_matrix[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 测试集比例哦
    train_data = np.column_stack((X_train, y_train))
    valid_data = np.column_stack((X_test, y_test))
    for jk in train_data:
        jk=jk[0]
        v6.write(jk+" "+" "+node_c[jk]+"\n")
    for key in class_cl:
         class_p=0
         for jk in valid_data:
             jk = jk[0]
             vw[jk] = 0.5
             val = str(vw[jk]) + "," +key
             v4.write(jk + " " + str(vw[jk]) + " " + node_c[jk] + "\n")
         for kk in train_data:
             kk = kk[0]  #
             if node_c[kk] == key:
                 tw[kk] = 1
             else:
                 tw[kk] = 0
         for bianli in range(1):#5次迭代
            zl=0
            fl=0
            aa = 0
            for j in valid_data: # 每个节点对每一类的P值
                j = j[0]  #
                v5.write(key+"\n")

                ww = 0
                ww2 = 0
                asso = node_n[j]

                for i in asso:
                    s1 = j + "," + i
                    s2 = i + "," + j
                    wei = 0
                    if s1 in weight:
                        wei = weight[s1]
                        v5.write(s1+" ")
                    else:
                        wei = weight[s2]
                        v5.write(s2 + " ")
                    if i in train_data:
                        ww2 = ww2 + float(wei)
                        v5.write("222train-weight-"+" "+str(i)+"关系节点i的类别："+node_c[i]+" "+str(ww2)+"\n")
                        if node_c[i] == key:
                            ww = ww + float(wei) * tw[i]
                            v5.write("wwtrain-weight-"+" "+str(i)+"关系节点i的类别："+node_c[i]+" "+str(ww)+"\n")

                    if i in valid_data:
                        ww = ww + float(wei) * vw[i]
                        ww2 = ww2 + float(wei)
                        v5.write("222valid-weight-" + " " + str(i) + " ww2 :" + str(ww2) + "\n")
                        v5.write("wwvalid-weight-" + " " + str(i) + " ww: " + str(ww) + "\n")
                v5.write(str(asso)+"\n")
                if ww2 == 0:
                    aa=aa+1
                    continue
                pvalue = ww / ww2

                v5.write(j + " 属于该类的概率：" + key +" 真实类别:"+node_c[j]+ " " + str(ww)+" 所有的权重和："+str(ww2)+"属于该类的概率："+str(pvalue) + "\n")
                vw[j] = ww / ww2
                v5.write(str(j)+" 新的vw "+str(vw[j])+"\n" + "\n")
                sum = sum + 1
         print(vw)
         for k in  vw:

            if k in wvrn:
                q = wvrn[k]
                qq=q.split(",")
                qq1 = qq[0]
                if vw[k] > float(qq1):
                    #print(vw[k])
                    #print(q)
                    kagi = str(vw[k]) + "," + key
                    wvrn[k] = kagi
            else:
                wvrn[k]=str(vw[k]) + "," + key
            #print(vw[k])
    wv =open('www.txt','w')
    for p in vw:
        s=wvrn[p]
        #print(s)
        cla=s.split(",")
        cla_c=cla[1]
        #print(cla)
        if node_num[p]==0:
            continue
        if cla_c==node_c[p]:
            zl=zl+1
        else:
            fl=fl+1
        wv.write(str(p) + " " + s + " "+node_c[str(p)]+ "\n")
    print(zl)
    print(fl)
    print(zl/(zl+fl))
        # 存储 节点，vw最大的值和类别，两个值都需要替换






