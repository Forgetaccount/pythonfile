from sklearn.model_selection import KFold
import math

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

class_cl=['ReinforcementLearning','RuleLearning','GeneticAlgorithms',
          'ProbabilisticMethods','Theory','CaseBased','NeuralNetworks'
    ]#3
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
p1=0
p2=0
p3=0
for jj in range(50):
    wri_valid = open('cc_valid.txt', 'w')  # 6
    train_data = []
    valid_data = []
    # 每个类按比例抽取
    for c in class_cl:
        list_class = []
        class_dict = {}  # 数字对应node的字典
        i = 0
        ii = 0
        for i in range(4240):  # 7 实体的个数-1  0--1440
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

    for k in valid_data:
        wri_valid.write(k)
        wri_valid.write(" ")
        wri_valid.write(node_c[k])
        wri_valid.write(" ")
        wri_valid.write(node_num[k])
        wri_valid.write("\n")
    wri_valid.close()
    wri_valid2=open('cc_train.txt','w') #8
    for k in train_data:
        wri_valid2.write(k)
        wri_valid2.write(" ")
        wri_valid2.write(node_c[k])
        wri_valid2.write(" ")
        wri_valid2.write(node_num[k])
        wri_valid2.write("\n")
    wri_valid2.close()

    fa3=open('cc_associate.txt', 'w')  #9
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
            fa3.write("\n")
            fa3.write(j)
            fa3.write("--")
            fa3.write(key)
            fa3.write("\n")
            fa3.write(str(asso))
            fa3.write("\n")
            for i in asso:
                if i in valid_data:
                    fa3.write("kout:")
                    fa3.write(i)
                    fa3.write("-------")

                    kout = kout + 1
                else:
                    if node_c[i] == key:
                        fa3.write("kin:")
                        fa3.write(i)
                        fa3.write("-------")
                        kin = kin + 1
                    else:
                        fa3.write("kout_!key:")
                        fa3.write(i)
                        fa3.write("-------")
                        kout = kout + 1

            ki = kin + kout
            fa3.write(str(ki))
            fa3.write("\n")

            for k in valid_data:
                D_s = int(node_num[k]) + D_s
            for k in train_data:
                cla = node_c[k]
                if cla == key:
                    Ds = int(node_num[k]) + Ds

                else:
                    D_s = int(node_num[k]) + D_s
            if ki==0:
                continue
            if kout == 0:
                p1=p1+1
                qi = 0
                x = fac[Ds]
                y = fac[D_s - ki]
                xx = fac[ki]
                yy = fac[D - 2 * ki]
                z = fac[D - ki]
                u1 = fac[kin]
                u3 = fac[Ds - kin]
                u4 = fac[D_s - ki - kout]
                p = x + y + yy + xx
                q = u1 + u3 + u4 + z
                pvalue = math.exp(p - q) * ((1 - math.pow(qi, kout + 1)) / (1 - qi))
                fa3.write('kin:' + str(kin) + ',kout:' + str(kout) + ',Ds:' + str(Ds) + ',D_s' + str(D_s) + "\n")
                fa3.write(" ")
                fa3.write(str(pvalue))
            elif kin == 0:
                x = fac[Ds]
                y = fac[D_s - ki]
                xx = fac[ki]
                yy = fac[D - 2 * ki]
                z = fac[D - ki]
                u2 = fac[kout]
                u3 = fac[Ds - kin]
                u4 = fac[D_s - ki - kout]
                p = x + y + yy + xx
                q =   u2 + u3 + u4 + z
                p3 = p3 + 1
                fa3.write('kin:' + str(kin) + ',kout:' + str(kout) + ',Ds:' + str(Ds) + ',D_s' + str(D_s) + "\n")
                pvalue = math.exp(p - q) * kout
                #pvalue = 1
                p2=p2+1
                fa3.write('kin:' + str(kin) + ',kout:' + str(kout) + ',Ds:' + str(Ds) + ',D_s' + str(D_s) + "\n")
                fa3.write(" ")
                fa3.write(str(pvalue))
            else:
                if ki==0:
                    continue
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
                qi = kout * (Ds - kin) / (kin * (D_s - kout))
                p3=p3+1
                fa3.write('kin:'+str(kin)+',kout:'+str(kout)+',Ds:'+str(Ds)+',D_s'+str(D_s)+"\n")
                pvalue = math.exp(p - q) * ((1 - math.pow(qi, kout + 1)) / (1 - qi))
                fa3.write(" ")
                fa3.write(str(pvalue))

            if pvalue < class_p:
                class_p = pvalue
                class_end = key
        sum = sum + 1
        if node_c[j] == class_end:
            zl = zl + 1
            fa3.write("\n")
            fa3.write(class_end)
            fa3.write(" ")
            fa3.write(str(zl))
            fa3.write("\n")
        fa3.write("\n")
        fa3.write("\n")
    fa3.write("\n")
    print(zl/sum)
    accu=accu+zl/sum

print(p1)
print(p2)
print(p3)