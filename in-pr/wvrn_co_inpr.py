from sklearn.model_selection import KFold
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


tw={}
vw={}
v4=open('v4.txt','w')
v5=open('v5.txt','w')
v6=open('v6.txt','w')
for jj in range(50):
    train_data = []
    valid_data = []
    # 每个类按比例抽取
    for c in class_cl:
        list_class = []
        class_dict = {}  # 数字对应node的字典
        i = 0
        ii = 0
        for i in range(2189):  # 7 实体的个数-1  0--1440
            no = num_c[i]  # num对应的node
            if node_c[no] == c:  # node对应的class是否为该类
                class_dict[ii] = no  # 该类 num_update=node
                list_class.append(no)  # 每类的个数
                ii = ii + 1
        kf = KFold(n_splits=10, shuffle=True)
        for train, valid in kf.split(list_class):
            for k in train:
                no = class_dict[k]
                train_data.append(no)
            for k in valid:
                no = class_dict[k]
                valid_data.append(no)
            break
    c1 = 0
    print(jj)
    c2 = 0
    count = 0
    for jk in valid_data:
        vw[jk] = 0.5
        #v4.write(jk+" "+str(vw[jk])+" "+node_c[jk]+"\n")
    #for jk in train_data:
       # v6.write(jk+" "+" "+node_c[jk]+"\n")
    for bianli in range(1):
        for j in valid_data:  # 具体哪个node
            class_end = ""
            class_p = 0
            for key in class_cl:  # 每个节点对每一类的P值
               # v5.write(key+"\n")
                for kk in train_data:
                    if node_c[kk] == key:
                        tw[kk] = 1
                    else:
                        tw[kk] = 0

                ww = 0
                ww2 = 0
                asso = node_n[j]

                for i in asso:
                    s1 = j + "," + i
                    s2 = i + "," + j
                    wei = 0
                    if s1 in weight:
                        wei = weight[s1]
                  #      v5.write(s1+" ")
                    else:
                        wei = weight[s2]
                 #       v5.write(s2 + " ")
                    if i in train_data:
                        ww2 = ww2 + float(wei)
                    #    v5.write("222train-weight-"+" "+str(i)+" "+str(ww2)+"\n")
                        if node_c[i] == key:
                            ww = ww + float(wei) * tw[i]
                   #         v5.write("wwtrain-weight-"+" "+str(i)+" "+str(ww)+"\n")

                    if i in valid_data:
                        ww = ww + float(wei) * vw[i]
                        ww2 = ww2 + float(wei)
                  #      v5.write("222valid-weight-" + " " + str(i) + " " + str(ww2) + "\n")
                 #       v5.write("wwvalid-weight-" + " " + str(i) + " " + str(ww) + "\n")
                #v5.write(str(asso)+"\n")
                if ww == 0:
                    continue
                pvalue = ww / ww2
                #v5.write(j + " " + key + " " + str(ww)+" "+str(ww2)+" "+str(pvalue) + "\n")
                #v5.write(str(class_p)+" "+class_end+" "+"\n")

                if pvalue > class_p:
                    class_p = pvalue
                    class_end = key
            #v5.write("\n"+"\n")
            sum = sum + 1
            if node_c[j] == class_end:
                zl = zl + 1
            if bianli==4:
                sum = sum + 1
                if node_c[j] == class_end:
                    zl = zl + 1
            if ww2==0:
                continue
            vw[j] = ww / ww2

    print(zl/sum)
    accu=accu+zl/sum
print(sum)
print(zl)
print(accu/50)

