from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import  numpy as np
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
          'Conglomerates','ConsumerCyclical','Services']#3
D = 23332#4

f2 = open('fac1.txt', 'r')  # 5
fac = {}
for line in f2.readlines():
    line = line.strip()
    s = line.split()
    fac[int(s[0])] = float(s[1])
f2.close()

jj = 0
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
        if kout >= 308:
            if qi > 1:
                pvalue = 1
            else:
                right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
                pvalue = math.exp(p - q) * right
        elif qi==1:
            pvalue=1
        else:
            #print("___________")
            #print(qi)
            #print(kout)

            right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
            pvalue = math.exp(p - q) * right
    return pvalue
for jj in range(7):
    class_cl = ['Technology', 'Healthcare', 'Financial', 'Energy', 'BasicMaterials',
                'CapitalGoods', 'Utilities', 'ConsumerNonCyclical', 'Transportation',
                'Conglomerates', 'ConsumerCyclical', 'Services']
    print(jj)
    train_data = []
    valid_data = []
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
        train, valid = train_test_split(list_class, test_size=0.8)
        for x in train:
            train_data.append(x)
        for y in valid:
            valid_data.append(y)

    valid_data1 = valid_data[:]
    unknown = valid_data[:]
    known = []
    known_data = {}
    node_accu = {}
    for j in unknown:
        node_accu[j] = "unknown"
    count = 0
    l2 = 0
    length = len(valid_data)
    l3 = length - l2
    class_cl.append("unknown")
    while l3 != 0:
        l2 = length
        # yuzhi=2#0.01/(length*8)
        # print(yuzhi)
        for j in unknown:  # 具体哪个node
            if j in known:
                continue
            pbb = {}
            for pb in class_cl:
                pbb[pb] = 0
            pbb["unknown"] = 0
            class_end = "unknown"
            asso = node_n[j]
            zlass = []
            for i in asso:
                if i in valid_data:
                    #  print(str(j) + " " + str(i) + " " + "unknown")
                    pbb["unknown"] = 1
                    if "unknown" in zlass:
                        continue
                    else:
                        zlass.append("unknown")
                else:
                    for cc in class_cl:

                        if i in known:
                            if known_data[i] == cc:
                                # print(str(j) + " " + str(i) + " " + str(known_data[i]))
                                pbb[cc] = 1
                                if cc in zlass:
                                    continue
                                else:
                                    zlass.append(cc)
                        else:
                            if node_c[i] == cc:
                                # print(str(j) + " " + str(i) + " " + str(node_c[i]))
                                pbb[cc] = 1
                                if cc in zlass:
                                    continue
                                else:
                                    zlass.append(cc)
            q = []
            for c in class_cl:
                q.append((pbb[c]) / len(zlass))
            n1 = float(q[0])
            n2 = float(q[1])
            n3 = float(q[2])
            n4 = float(q[3])
            n5 = float(q[4])
            n6 = float(q[5])
            n7 = float(q[6])
            n8 = float(q[7])
            n9 = float(q[8])
            n10 = float(q[9])
            n11 = float(q[10])
            n12 = float(q[11])
            n13 = float(q[12])
            p = np.array([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13])
            # print(class_cl)
            # print(p)
            index = np.random.choice(class_cl, p=p.ravel())
            known_data[j] = index
            node_accu[j] = index
            count = count + 1
            # print("index:"+index)
            if index != "unknown":
                valid_data.remove(j)
                known.append(j)
            # tt.write(j + " 判断类别: " + class_end + " 实际类别:" + node_c[j] + "\n" + "\n" + "\n")
        length = len(valid_data)
        l3 = length - l2
        print(len(valid_data))
    print("count:" + str(count))
    class_cl.remove("unknown")
    kk = 0
    for kk in range(5):
        count1 = 0
        print(kk)
        kk = kk + 1
        for j in unknown:  # 具体哪个node
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
                # tt.write(j + " " + key + " " + str(kin) + " " + str(kout) + " " + str(Ds) + " " + str(D_s) + " " + str(
                #    pvalue) + "\n")
                if pvalue < class_p:
                    class_p = pvalue
                    class_end = key
            if node_accu[j] != class_end:
                count1 = count1 + 1
                # print(node_accu[j]+" "+class_end)

            known_data[j] = class_end
            node_accu[j] = class_end
            if class_end == "unknown":
                if j in known:
                    known.remove(j)
            else:
                if j in known:
                    continue
                else:
                    known.append(j)

        print("count1:" + str(count1))
        if count1 == 0:
            break
    sum = 0
    zl = 0
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
print(accu / 10)