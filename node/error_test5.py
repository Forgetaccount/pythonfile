from sklearn.model_selection import KFold
import math
#建立字典 node_n  node_num
f=open('cora_cite_node_num_n.txt','r')#1
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
#12 class

class_cl=['ProbabilisticMethods','Theory','CaseBased','NeuralNetworks','GeneticAlgorithms'
    ,'RuleLearning','ReinforcementLearning']#3
D = 22516#4

wri_valid = open('cora_cite_valid.txt', 'w')  # 5
train_data = []
valid_data = []
# 每个类按比例抽取

f2 = open('cora_cite_fac1.txt', 'r')  # 6
fac = {}
fac[0] = 1
for line in f2.readlines():
    line = line.strip()
    s = line.split()
    fac[int(s[0])] = float(s[1])
f.close()
w1 = open('w1.txt', 'w')
w2 = open('w2.txt', 'w')
w3 = open('w3.txt', 'w')
for c in class_cl:
    list_class = []
    class_dict = {}  # 数字对应node的字典
    i = 0
    ii = 0
    for i in range(4240):  # 7  实体的个数-1  0--1440
        no = num_c[i]  # num对应的node
        if node_c[no] == c:  # node对应的class是否为该类
            class_dict[ii] = no  # 该类 num_update=node
            list_class.append(no)  # 每类的个数
            w1.write(str(ii))
            w1.write(" ")
            w1.write(no)
            w1.write(" ")
            w1.write(node_c[no])
            w1.write(" ")
            w1.write(node_num[no])
            w1.write("\n")
            ii = ii + 1
    kf = KFold(n_splits=5, shuffle=True)
    for train, valid in kf.split(list_class):
        for k in train:
            no = class_dict[k]
            train_data.append(no)
            w3.write(str(k))
            w3.write(" ")
            w3.write(no)
            w3.write(" ")
            w3.write(node_num[no])
            w3.write("\n")
        for k in valid:
            no = class_dict[k]
            valid_data.append(no)
            w2.write(str(k))
            w2.write(" ")
            w2.write(no)
            w2.write(" ")
            w2.write(node_num[no])
            w2.write("\n")
        break

for k in valid_data:
    wri_valid.write(k)
    wri_valid.write(" ")
    wri_valid.write(node_c[k])
    wri_valid.write("\n")
w2.close()
w1.close()
w3.close()
wri_valid.close()


jj = 0
zl = 0
sum = 0
accu = 0
tt= open('true.txt', 'w')
for jj in range(3):
    print(jj)
    for j in valid_data:  # 具体哪个node
        class_end = ""
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
                else:
                    if node_c[i] == key:
                        kin = kin + 1
                    else:
                        kout = kout + 1
            ki = kin + kout
            for k in valid_data:
                D_s = int(node_num[k]) + D_s
            for k in train_data:
                cla = node_c[k]
                if cla == key:
                    Ds = int(node_num[k]) + Ds
                else:
                    D_s = int(node_num[k]) + D_s

            x = fac[Ds]
            y = fac[D_s - ki]
            xx = fac[ki]
            yy = fac[D - 2 * ki]
            z = fac[D - ki]
            u1 = fac[kin]
            u2 = fac[kout]
            u3 = fac[Ds - kin]
            u4 = fac[D_s - ki - kout]
            p = x + y + yy + xx
            q = u1 + u2 + u3 + u4 + z
            # print(p-q)
            if kin == 0:
                pvalue=1
            elif kout== 0:
                pvalue = math.exp(p - q)
            else:
                qi = kout * (Ds - kin) / (kin * (D_s - kout))
                pvalue = math.exp(p - q) * (1 - math.pow(qi, kout + 1) / (1 - qi))
            if pvalue < class_p:
                class_p = pvalue
                class_end = key

            tt.write(j + " " + key + " "+str(kin)+" "+str(kout)+" "+str(Ds)+" "+str(D_s)+" "+str(pvalue)+"\n")
            tt.write(str(asso)+"\n")
        sum = sum + 1
        if node_c[j] == class_end:
            zl = zl + 1
    print(zl/sum)
    accu = accu + zl / sum
print(sum)
print(zl)