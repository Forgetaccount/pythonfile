from scipy import stats
from sklearn.model_selection import train_test_split
import numpy as np
f=open('industry_yh_node_num_n.txt','r')#1
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

f1=open('industry_yh_class.txt','r')#2
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
          'Conglomerates','ConsumerCyclical','Services']#3
D = 28292#4

accu=0
for jj in range(100):
    zl = 0
    sum = 0
    train_data = []
    valid_data = []
    for c in class_cl:
        list_class = []
        class_dict = {}  # 数字对应node的字典
        i = 0
        ii = 0
        for i in range(1798):  # 7 实体的个数-1  0--1440
            no = num_c[i]  # num对应的node
            if node_c[no] == c:  # node对应的class是否为该类
                class_dict[ii] = no  # 该类 num_update=node
                list_class.append(no)  # 每类的个数
                ii = ii + 1
        train, valid = train_test_split(list_class, test_size=0.2)
        for x in train:
            train_data.append(x)
        for y in valid:
            valid_data.append(y)

    for j in valid_data:
        class_p=1
        class_cc="unknown"
        for key in class_cl:
            Db = 0
            kin=0
            for t in train_data:
                if node_c[t]==key:
                    Db=Db+int(node_num[t])
            pb=Db/D
            du=int(node_num[j])
            asso = node_n[j]
            for a in asso:
                if a in train_data:
                    if node_c[a]==key:
                        kin=kin+1
            kk = np.arange(0, du+1)
            bin=stats.binom.cdf(kk,du,pb)
            b=bin[kin]
            pvalue=1-b
            if pvalue<class_p:
                class_p=pvalue
                class_cc=key
        sum=sum+1
        if class_cc==node_c[j]:
            zl=zl+1
    accu=accu+zl/sum
    print(jj)
    print(zl/sum)
print(zl)
print(sum)
print(zl/sum)
print(accu/100)