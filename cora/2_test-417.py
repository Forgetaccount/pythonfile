from sklearn.model_selection import KFold
import math
from scipy import stats
from sklearn.model_selection import train_test_split
import numpy as np
f=open('cora_cite_node_num_n.txt','r')#1
f=open('cora_wuguli.txt','r')
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

f1=open('cora_wuguliclass.txt','r')#2
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

class_cl=['ProbabilisticMethods','Theory','CaseBased','NeuralNetworks','GeneticAlgorithms'
    ,'RuleLearning','ReinforcementLearning']#3
D = 22516#4

f2 = open('fac1.txt', 'r')  # 5
fac = {}
for line in f2.readlines():
    line = line.strip()
    s = line.split()
    fac[int(s[0])] = float(s[1])
f2.close()

jj = 0
zl = 0
sum = 0
accu = 0

def jc(kin,kout,D_s,Ds):
    ki = kin + kout
    x = fac[Ds]
    y = fac[D_s - ki]
    if ki!=0:
        xx = fac[ki]
    yy = fac[D - 2 * ki]
    z = fac[D - ki]
    if kin != 0:
        u1 = fac[kin]
    if kout != 0:
        u2 = fac[kout]
    u3 = fac[Ds - kin]
    u4 = fac[D_s - ki - kout]
    # print((1 - math.pow(qi, kout + 1)) / (1 - qi))
    if kin==0:
        pvalue = 1
    elif kout==0:
        p = x + y + yy + xx
        q = u1 + u3 + u4 + z
        pvalue = math.exp(p - q)
    else:
        p = x + y + yy + xx
        q = u1 + u2 + u3 + u4 + z
        qi = kout * (Ds - kin) / (kin * (D_s - kout))

        #print(kout)
        if kout==308:
            pvalue=1
        elif kout==310:
            pvalue=1
        elif kout == 307:
            pvalue = 1
        elif kout==309:
            pvalue=1
        else:
            #print("___________")
            #print(p)
            #print(qi)
            #print(kout)
            #print(1 - math.pow(qi, kout + 1))
            #print(1 - qi)
            right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
            pvalue = math.exp(p - q) * right
    return pvalue

accu=0
for jj in range(50):
    train_data = []
    valid_data = []
    for c in class_cl:
        list_class = []
        class_dict = {}  # 数字对应node的字典
        i = 0
        ii = 0
        for i in range(3583):  # 7 实体的个数-1  0--1440
            no = num_c[i]  # num对应的node
            if node_c[no] == c:  # node对应的class是否为该类
                class_dict[ii] = no  # 该类 num_update=node
                list_class.append(no)  # 每类的个数
                ii = ii + 1
        train, valid = train_test_split(list_class, test_size=0.5)
        for x in train:
            train_data.append(x)
        for y in valid:
            valid_data.append(y)

    print(jj)
    len1=len(valid_data)
    count = 0
    known=[]
    known_data = {}
    length=len(valid_data)
    print(length)
    unknown = valid_data[:]
    node_unknown=[]
    for v in valid_data:
        node_unknown.append(v)
    length=len(node_unknown)
    l2=0
    l3=length-l2
    node_accu={}
    for j in unknown:
        node_accu[j] = "unknown"
    count=0
    while l3!=0:
        l2=length
        yuzhi=0.01/(length*8)
        print(yuzhi)
        for j in unknown:  # 具体哪个node
            if j in known:
                continue
            class_end = "unknown"
            class_p = 1
            for key in class_cl:  # 每个节点对每一类的P值
                Db = 0
                kin = 0
                for t in train_data:
                    if node_c[t] == key:
                        Db = Db + int(node_num[t])
                pb = Db / D
                du = int(node_num[j])
                asso = node_n[j]
                for a in asso:
                    if a in train_data:
                        if node_c[a] == key:
                            kin = kin + 1
                kk = np.arange(0, Db)
                bin = stats.binom.cdf(kk, du, pb)
                b = bin[kin]
                pvalue = 1 - b

                tt.write(j + " " + key + " " + str(kin) +" "+ str(pvalue) + "\n")
                if pvalue < class_p:
                    class_p = pvalue
                    class_end = key
                    node_accu[j] = key
            if class_p < yuzhi:
                known_data[j] = class_end
                count=count+1
                valid_data.remove(j)
                known.append(j)
                if j in node_unknown:
                    node_unknown.remove(j)
            tt.write(j + " 判断类别: " + class_end + " 实际类别:" + node_c[j] + "\n" + "\n" + "\n")
        length=len(node_unknown)
        l3 = length - l2
        print(len(node_unknown))
        tt.write("zaiyici")
    print("count:"+str(count))

    l3=len(node_unknown)
    unknown=node_unknown[:]
    l4=0
    l5=l3-l4
    while l5!=0:
        l4=len(node_unknown)
        for j in unknown:  # 具体哪个node
            if j in known:
                continue
            class_end = "unknown"
            class_p = 1
            for key in class_cl:  # 每个节点对每一类的P值
                Db = 0
                kin = 0
                for t in train_data:
                    if node_c[t] == key:
                        Db = Db + int(node_num[t])
                pb = Db / D
                du = int(node_num[j])
                asso = node_n[j]
                for a in asso:
                    if a in train_data:
                        if node_c[a] == key:
                            kin = kin + 1
                kk = np.arange(0, Db)
                bin = stats.binom.cdf(kk, du, pb)
                b = bin[kin]
                pvalue = 1 - b

                if pvalue < class_p:
                    class_p = pvalue
                    class_end = key
                    node_accu[j] = key
            if class_end == "unknown":
                continue
            else:
                if j in node_unknown:
                    known_data[j] = class_end
                    valid_data.remove(j)
                    known.append(j)
                    node_unknown.remove(j)
            tt.write(j + " 判断类别: " + class_end + " 实际类别:" + node_c[j] + "\n" + "\n" + "\n")
        break
        l3 = len(node_unknown)
        l5 = l4 - l3
        print("l5:"+str(l5))
    sum=0
    zl=0
    print(len(node_unknown))
    for a in node_accu:
        sum = sum + 1
        class_end=node_accu[a]
        aa.write(str(a)+" "+str(class_end)+"\n")
        if node_c[a] == class_end:
            zl = zl + 1
    print(zl/sum)
    accu=accu+zl/sum
print(sum)
print(zl)
print(accu/50)