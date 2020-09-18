
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import math
fff=open('aaaaadxx.txt','r')#1

f=open('aaaaadxx.txt','r')
node_num={}#node---num
node_n={}#node---asso
for line in f.readlines():
    line=line.strip()
    s=line.split()
    x=s[0]
    pinjie=s

    del(pinjie[0])
    del(pinjie[0])
    node_n[x]=pinjie
f.close()
for line in fff.readlines():
    line = line.strip()
    s = line.split()
    x = s[0]
    pinjie = s
    node_num[s[0]] = s[1]
f.close()
f1=open('cora_cite_class.txt','r')#2
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
accu = 0
tt=open('true.txt','w')
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
        if kout>=190:
            pvalue=1
        elif qi==1:
            pvalue=1
        else:
            print(kout)
            print(qi)
            right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
            pvalue = math.exp(p - q) * right
    return pvalue
for jj in range(1):
    zl = 0
    sum = 0
    train_data = []
    valid_data = []
    # 每个类按比例抽取
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
        train, valid = train_test_split(list_class, test_size=0.8)
        for x in train:
            train_data.append(x)
        for y in valid:
            valid_data.append(y)
    print(jj)
    len1 = len(valid_data)
    count = 0
    known = []
    known_data = {}

    length = len(valid_data)
    print(length)

    unknown = valid_data[:]
    node_unknown = []
    for v in valid_data:
        node_unknown.append(v)
    length = len(node_unknown)
    l2 = 0
    l3 = length - l2
    node_accu = {}
    for j in unknown:
        node_accu[j] = "unknown"
    count = 0
    while l3 != 0:
        l2 = length
        yuzhi = 0.01 / (length * 13)
        print(yuzhi)
        for j in unknown:  # 具体哪个node
            if j in known:
                continue
            class_end = "unknown"
            class_p = 1
            for key in class_cl:  # 每个节点对每一类的P值
                kin = 0
                kout = 0
                D_s = 0
                Ds = 0
                asso = node_n[j]
                for i in asso:
                    if i in valid_data:
                        kout = kout + 1
                    elif i in known:
                        if known_data[i] == key:
                            kin = kin + 1
                        else:
                            kout = kout + 1
                    else:
                        if node_c[i] == key:
                            kin = kin + 1
                        else:
                            kout = kout + 1
                for k in valid_data:
                    D_s = int(node_num[k]) + D_s
                for k in train_data:
                    cla = node_c[k]
                    if cla == key:
                        Ds = int(node_num[k]) + Ds
                    else:
                        D_s = int(node_num[k]) + D_s
                for k in known:
                    cla = known_data[k]
                    if cla == key:
                        Ds = int(node_num[k]) + Ds
                    else:
                        D_s = int(node_num[k]) + D_s
                pvalue = jc(kin, kout, D_s, Ds)
                if pvalue < class_p:
                    class_p = pvalue
                    class_end = key
                    node_accu[j] = key
                tt.write(j + " " + key + " "+node_c[j]+" " + str(kin) + " " + str(kout) + " " + str(Ds) + " " + str(D_s) + " " + str(
                pvalue) + "\n")
            tt.write(j+" "+ class_end +"\n"+"\n")
            if class_p < yuzhi:
                known_data[j] = class_end
                count = count + 1
                valid_data.remove(j)
                known.append(j)
                if j in node_unknown:
                    node_unknown.remove(j)
        length = len(node_unknown)
        l3 = length - l2
    unknown = node_unknown[:]
    l4 = len(node_unknown)
    for j in unknown:  # 具体哪个node
        if j in known:
            continue
        class_end = "unknown"
        class_p = 1
        for key in class_cl:  # 每个节点对每一类的P值
            kin = 0
            kout = 0
            D_s = 0
            Ds = 0
            asso = node_n[j]
            for i in asso:
                if i in valid_data:
                    kout = kout + 1
                elif i in known:
                    if known_data[i] == key:
                        kin = kin + 1
                    else:
                        kout = kout + 1
                else:
                    if node_c[i] == key:
                        kin = kin + 1
                    else:
                        kout = kout + 1
            for k in valid_data:
                D_s = int(node_num[k]) + D_s
            for k in train_data:
                cla = node_c[k]
                if cla == key:
                    Ds = int(node_num[k]) + Ds
                else:
                    D_s = int(node_num[k]) + D_s
            for k in known:
                cla = known_data[k]
                if cla == key:
                    Ds = int(node_num[k]) + Ds
                else:
                    D_s = int(node_num[k]) + D_s
            pvalue = jc(kin, kout, D_s, Ds)
            if kin == 0:
                continue
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
    l4 = len(node_unknown)
    print(len(node_unknown))
    sum=0
    zl=0
    for a in node_accu:
        sum = sum + 1
        class_end = node_accu[a]
        if node_c[a] == class_end:
            zl = zl + 1
    print(zl / sum)
    accu = accu + zl / sum
    # ff.write(str(c1) +" "+str(c2)+ " " + str(count) + " 4240 " +str(zl/sum)+"\n")
print(sum)
print(zl)
print(zl / len1)
print(accu / 30)