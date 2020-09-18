from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import numpy as np
import math
#计算pvalue
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
#f1=open('cora_cite_class.txt','r')
f1=open('cora_wuguliclass.txt','r')
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
    ,'RuleLearning','ReinforcementLearning']

D = 30462#4

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
        if kout>=308:
            pvalue=1
        elif qi==1:
            pvalue=1
        else:
            right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
            pvalue = math.exp(p - q) * right
    return pvalue

zidian={'ProbabilisticMethods':0,'Theory':0,'CaseBased':0
        ,'NeuralNetworks':0,'GeneticAlgorithms':0,'RuleLearning':0
        ,'ReinforcementLearning':0}

def M(known,train_data):
    for s_i in known:
        if known_data[s_i]=='ProbabilisticMethods':
            zidian['ProbabilisticMethods']=zidian['ProbabilisticMethods']+1
        if known_data[s_i] == 'Theory':
            zidian['Theory'] = zidian['Theory'] + 1
        if known_data[s_i]=='CaseBased':
            zidian['CaseBased'] = zidian['CaseBased'] + 1
        if known_data[s_i] == 'NeuralNetworks':
            zidian['NeuralNetworks'] = zidian['NeuralNetworks'] + 1
        if known_data[s_i]=='GeneticAlgorithms':
            zidian['GeneticAlgorithms'] = zidian['GeneticAlgorithms'] + 1
        if known_data[s_i] == 'RuleLearning':
            zidian['RuleLearning'] = zidian['RuleLearning'] + 1
        if known_data[s_i]=='ReinforcementLearning':
            zidian['ReinforcementLearning'] = zidian['ReinforcementLearning'] + 1
    for s_i in train_data:
        if node_c[s_i] == 'ProbabilisticMethods':
            zidian['ProbabilisticMethods'] = zidian['ProbabilisticMethods'] + 1
        if node_c[s_i] == 'Theory':
            zidian['Theory'] = zidian['Theory'] + 1
        if node_c[s_i] == 'CaseBased':
            zidian['CaseBased'] = zidian['CaseBased'] + 1
        if node_c[s_i] == 'NeuralNetworks':
            zidian['NeuralNetworks'] = zidian['NeuralNetworks'] + 1
        if node_c[s_i] == 'GeneticAlgorithms':
            zidian['GeneticAlgorithms'] = zidian['GeneticAlgorithms'] + 1
        if node_c[s_i] == 'RuleLearning':
            zidian['RuleLearning'] = zidian['RuleLearning'] + 1
        if node_c[s_i] == 'ReinforcementLearning':
            zidian['ReinforcementLearning'] = zidian['ReinforcementLearning'] + 1
    return zidian
s_k=3583
F=((s_k)*(s_k)-(s_k))/2
s_n=23332
M_M=0


def jac(s_i,linju):
    lj1=node_n[s_i]
    lj2=node_n[linju]
    lj3=list(set(lj1) & set(lj2))
    lj4=list(set(lj1).union(set(lj2)))

 #   kk.write(str(lj1)+" "+"\n"+str(lj2)+" "+"\n\n\n")
    return len(lj3)/len(lj4)

#kk=open('quanbu.txt','w')

for jj in range(1):

    class_cl = ['ProbabilisticMethods', 'Theory', 'CaseBased', 'NeuralNetworks', 'GeneticAlgorithms'
        , 'RuleLearning', 'ReinforcementLearning']
    print(jj)
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
        train, valid = train_test_split(list_class, test_size=0.2)
        for x in train:
            train_data.append(x)
        for y in valid:
            valid_data.append(y)
    valid_data1 = valid_data[:]
    unknown = valid_data[:]
    known = []
    known_data = {}
    node_accu={}
    for j in unknown:
        node_accu[j] = "unknown"
    count=0
    l2 = 0
    length = len(valid_data)
    l3 = length - l2
    while l3!=0:
        l2=length
       # yuzhi=2#0.01/(length*8)
       # print(yuzhi)
        for j in unknown:  # 具体哪个node
            if j in known:
                continue
            pbb = {}
            for pb in class_cl:
                pbb[pb] = 0
            class_end = "unknown"
            asso = node_n[j]
            zlass=[]
            for i in asso:
                if i in valid_data:
                    continue
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
                if len(zlass) == 0:
                    q.append(1/7)
                    q.append(1/7)
                    q.append(1/7)
                    q.append(1/7)
                    q.append(1/7)
                    q.append(1/7)
                    q.append(1/7)
                    break
                q.append((pbb[c]) / len(zlass))
            n1 = float(q[0])
            n2 = float(q[1])
            n3 = float(q[2])
            n4 = float(q[3])
            n5 = float(q[4])
            n6 = float(q[5])
            n7 = float(q[6])
            if len(zlass)==0:
                n1=1/7
                n2=1/7
                n3=1/7
                n4 =1/7
                n5 = 1/7
                n6 =1/7
                n7=1/7
            p = np.array([n1, n2, n3, n4, n5, n6,n7])
            #print(p)
            index = np.random.choice(class_cl, p=p.ravel())
            known_data[j] = index
            node_accu[j] = index
            count = count + 1
            if index!="unknown":
                valid_data.remove(j)
                known.append(j)
 #               kk.write(str(j)+" 随机类别:"+known_data[j]+"\n")
        length=len(valid_data)
        l3 = length - l2
    zidian=M(known,train_data)
   # print(known_data)
 #   kk.write("\n\n\n下一步："+"\n")
    m=0
    for s_i in known_data:
        s_lj=node_n[s_i]
        for node_accu in s_lj:
            if node_accu in known_data:
                if known_data[node_accu]==known_data[s_i]:
                    m=m+1
            if node_accu in train_data:
                if node_c[node_accu]==known_data[s_i]:
                    m=m+1
    for s_i in train_data:
        s_lj = node_n[s_i]
        for node_accu in s_lj:
            if node_accu in known_data:
                if known_data[node_accu]==node_c[s_i]:
                    m=m+1
            if node_accu in train_data:
                if node_c[node_accu]==node_c[s_i]:
                    m=m+1
    #print(m)
    q1=m/s_n
    #print(q1)
  #  kk.write("下面的是每个类别的顶点个数s_i")
    for s_i in zidian:
 #       kk.write(str(zidian[s_i])+"  ")
        M_M=M_M+((zidian[s_i])*(zidian[s_i])-(zidian[s_i]))/2
    #print(M_M)
    q2=M_M/F
    #print(F)
    #print(q2)
    surprise=q1*math.log(q1/q2,math.e)+(1-q1)*(math.log((1-q1)/(1-q2),math.e))
    print("sur:")
    print(surprise)
    #print(len(known))
    cishu=0
 #   kk.write("\n\n\n"+str(m)+" ---  "+str(s_n)+" --- "+str(M_M)+" --- "+str(F)+"\n")#????????????????????????
    for cishu in range(0,10):
        M_M=0
        class_ed = ""
        cishu=cishu+1
        for s_i in unknown:
            class_ed=known_data[s_i]
            class_j=known_data[s_i]
            linju=node_n[s_i]
            ja=0
            jaccard=0
            for lj in linju:#比较待分类节点和其它邻居节点的相似度

                jaccard=jac(s_i,lj)

                if jaccard>ja:
                    ja=jaccard
                    if lj in known_data:
                        class_j=known_data[lj]
                    if lj in train_data:
                        class_j=node_c[lj]
  #              kk.write(str(s_i) + "--- " + str(lj) + "--- " + str(jaccard) + "--- " + str(ja) + "\n\n")
            known_data[s_i]=class_j
            if class_ed==class_j:
                continue
            else:
                zidian[class_ed] = zidian[class_ed] - 1#原来的类别
                zidian[class_j]=zidian[class_j]+1#现在的类别
                m=m-int(node_num[s_i])
                lj5=node_n[s_i]

  #              kk.write(str(s_i)+"   原类别:"+class_ed+"   现类别:"+class_j+"\n")
                for i in lj5:#比较每个邻居，增删m
                    if i in train_data:
                        if node_c[i]==class_j:
                            m=m+1
                    if s_i in known:
                        if known_data[s_i]==class_j:
                            m=m+1
        for s_i in zidian:
            M_M = M_M + ((zidian[s_i]) * (zidian[s_i]) - (zidian[s_i])) / 2
        q1 = m / s_n   #p/m
        q2 = M_M / F   #M/F
        #print((1 - q1) * (math.log((1 - q1) / (1 - q2))))
        surprise =s_n*(q1 * math.log(q1 / q2) + (1 - q1) * (math.log((1 - q1) / (1 - q2))))
        print("---")
        print(surprise)
  #  kk.write("\n\n\n" + str(m) + " ---  " + str(s_n) + " --- " + str(M_M) + " --- " + str(F) + "\n")
   # print(zidian)
    sum=0
    zl=0
    true= open('true.txt', 'w')
    false=open('false','w')
    for a in unknown:
        sum = sum + 1
        class_end=known_data[a]
       # print(str(a)+" "+str(known_data[a])+" "+str(node_c[a]))
        if node_c[a] == class_end:
            zl = zl + 1
            true.write(str(a)+" "+node_c[a]+" "+class_end+"\n")
        else:
 #           print(str(a)+" "+node_c[a]+" "+class_end)
            false.write(str(a)+" "+node_c[a]+" "+class_end+"\n")
    print(zl/sum)
    print(zl)
    print(sum)
    accu=accu+zl/sum
#print("数据集Washington 测试集比例:0.8 按随机概率初始化类别 20次分类准确率的平均值:")
#print(accu/20)