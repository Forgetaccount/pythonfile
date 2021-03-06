from sklearn.model_selection import train_test_split
import math
print('pvalue方法 数据集：Washington 测试集比例：20%   重复进行实验20次')
f=open('washingco_node_num_n.txt','r')
#我们以Washington数据集为例介绍本文实现的方法：
node_num={}    #1-44行是将节点的类别和邻居存储到字典中
node_n={}
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
#f1=open('cora_cite_class.txt','r')
f1=open('class.txt','r')
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

class_cl=['student','course','faculty','department','project','staff'    ]

D = 30462#4

f2 = open('fac1.txt', 'r')  # 5
fac = {}
for line in f2.readlines():
    line = line.strip()
    s = line.split()
    fac[int(s[0])] = float(s[1])
f2.close()

jj = 0
accu = 0

def jc(kin,kout,D_s,Ds):   #该函数是根据公式用来计算每个节点针对每个类别的p值的
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
        if kout>=308:
            pvalue=1
        elif qi==1:
            pvalue=1
        else:
            right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
            pvalue = math.exp(p - q) * right
    return pvalue
ff=open('yh_count.txt','w')

for jj in range(20):       #在实验中，我们重复实验20次
    zl = 0
    sum = 0
    train_data = []
    valid_data = []
    for c in class_cl:
        list_class = []
        class_dict = {}
        i = 0
        ii = 0
        for i in range(434):
            no = num_c[i]
            if node_c[no] == c:
                class_dict[ii] = no  # 85-100行是划分训练集和测试集
                list_class.append(no)
                ii = ii + 1                      #修改测试集比例
        train, valid = train_test_split(list_class, test_size=0.2)
        for x in train:
            train_data.append(x)
        for y in valid:
            valid_data.append(y)
    print(jj)
                                     #下部分为本文设计的算法的代码
    len1=len(valid_data)
    count = 0
    known=[]
    known_data = {}
    length=len(valid_data)
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
    while l3!=0:                        #此处while循环用来进行主动学习
        l2=length
        yuzhi=0.01/(length*7)           #此处设置的是FWER阈值
        for j in unknown:
            if j in known:
                continue
            class_end = "unknown"
            class_p = 1
            for key in class_cl:       #每个节点针对每一个类别计算P值
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
            if class_p < yuzhi:
                known_data[j] = class_end
                count=count+1
                valid_data.remove(j)
                known.append(j)
                if j in node_unknown:
                    node_unknown.remove(j)
        length=len(node_unknown)
        l3 = length - l2
    l3=len(node_unknown)
    unknown=node_unknown[:]
    l4=0
    l5=l3-l4
    while l5!=0:        #此处while循环对还没有进行分类的节点进行强制分类
        l4=len(node_unknown)
        for j in unknown:
            if j in known:
                continue
            class_end = "unknown"
            class_p = 1
            for key in class_cl:
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
        break
    sum=0       #所有待分类节点的个数
    zl=0        #正确分类节点的个数
    for a in node_accu:
        sum = sum + 1
        class_end=node_accu[a]
        if node_c[a] == class_end:
            zl = zl + 1
    print(zl/sum)
    accu=accu+zl/sum
print("20次分类准确率的平均值:")
print(accu/20)