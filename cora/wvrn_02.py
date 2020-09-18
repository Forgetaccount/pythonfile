from sklearn.model_selection import train_test_split
print('wvRN方法——数据集：Cora 测试集比例：40%   实验20次')
f=open('cora_wuguli.txt','r')
f=open('cora_cite_node_num_n.txt','r')
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
f1=open('cora_cite_class.txt','r')
#f1=open('cora_wuguliclass.txt','r')
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
weight={}
ff=open('cora_cite_weight.txt','r')#2
for line in ff.readlines():
    line=line.strip()
    s=line.split(",")
    pinjie=s[0]+","+s[1]
    weight[pinjie] = s[2]
jj = 0
accu = 0
#cc=open('del.txt','w')
#cc2=open('del1.txt','w')
for jj in range(20):
    vw = {}
    print(jj)
    wvrn = {}
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
                # v5.write(str(ii) + " " + no + " " + node_c[no] + " " + node_num[no] + "\n")
                ii = ii + 1
        train, valid = train_test_split(list_class, test_size=0.2)
        for x in train:
            train_data.append(x)
        for y in valid:
            valid_data.append(y)
    for key in class_cl:
         vw = {}
         for jk in valid_data:#对每个节点进行属于该类的概率初始化
             ww = 0
             ww2 = 0
             asso = node_n[jk]
             #cc.write(str(jk) + " " )
             for i in asso:
                 s1 = jk + "," + i
                 s2 = i + "," + jk
                 wei = 0
                 if s1 in weight:
                     wei = weight[s1]
                 else:
                     wei = weight[s2]
                 ww2 = ww2 + float(wei)
                 if i in train_data:
                     if node_c[i] == key:
                         ww = ww + float(wei)
                  #   cc.write("train:" + str(i) + " " + node_c[i] + " " + str(wei) + " \n ")
                 #else:

                   # cc.write("valid:" +str(i)+" "+node_c[i]+" "+str(wei)+" - "+"\n")
             if ww==0:
                 vw[jk]=0
             else:
                 vw[jk] = ww/ww2
         #    cc.write("\n"+str(ww)+" "+str(ww2)+" 真实类别:"+node_c[jk]+" "+str(vw[jk])+" "+key+"\n"+"\n")
        # cc.write("\n"+"\n")
        # cc.write("abcdefg"+"\n")
         for bianli in range(1):#5次迭代
            for j in valid_data: # 每个节点对每一类的P值
                ww = 0
                ww2 = 0
                asso = node_n[j]

               # cc.write(str(j)+" ")
                for i in asso:
                    s1 = j + "," + i
                    s2 = i + "," + j
                    wei = 0
                    if s1 in weight:
                        wei = weight[s1]
                    else:
                        wei = weight[s2]
                    if i in train_data:
                        ww2 = ww2 + float(wei)
                        if node_c[i] == key:
                            ww = ww + float(wei)
                    if i in valid_data:
                        ww = ww + float(wei) * vw[i]
                        ww2 = ww2 + float(wei)
                  #  cc.write("asso:"+str(i)+" "+node_c[i]+" ww: "+str(ww)+" ww2: "+str(ww2)+"\n")

                if ww==0:
                    vw[j]=0
                else:
                    vw[j] = ww / ww2
                if j in wvrn:
                    q = wvrn[j]
                    qq = q.split(",")
                    qq1 = qq[0]
                    if vw[j] > float(qq1):
                        kagi = str(vw[j]) + "," + key
                        wvrn[j] = kagi
                else:
                    wvrn[j] = str(vw[j]) + "," + key
                #cc.write("\n" + " ww: " + str(ww) + " ww2: " + str(ww2)+"vw:"+str(vw[j])+" "+key+"\n"+"\n")
   # wv =open('www.txt','w')
    zl = 0
    sum = 0
    for p in wvrn:
        sum=sum+1
        s = wvrn[p]
        cla = s.split(",")
        cla_c = cla[1]
        pvalue=float(cla[0])
        if cla_c == node_c[p]:
            zl = zl + 1

    #    wv.write(str(p)+" "+cla_c+" "+str(node_c[p])+"\n")
   # print(len(wvrn))
    #print(zl)
    #print(sum)
    #print("第"+str(jj+1)+"次分类准确率："+str(zl/sum))
    print(zl/sum)
    accu=accu+zl/sum
    #print(len(train_data))
        # 存储 节点，vw最大的值和类别，两个值都需要替换
print('20次准确率的平均值：')
print(accu/20)





