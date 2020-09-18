import numpy as np
from sklearn.model_selection import train_test_split
#from sklearn.model_selection import KFold
import math
f=open('imdb_prodco_node_num_n.txt','r')#1
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

f1=open('imdb_prodco_class.txt','r')#2
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

class_cl=['NOTblockBuster','blockBuster']
D = 40634#4

f2 = open('imdb_prodco_fac1.txt', 'r')  # 5
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
        #print(qi)
        #print(kout)
        if kout==310:
            pvalue=1
        else:

            right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
            pvalue = math.exp(p - q) * right
    return pvalue

#w1 = open('w1.txt', 'w')
#w2 = open('w2.txt', 'w')
#w3 = open('w3.txt', 'w')
#tt=open('true.txt','w')

my_matrix = np.loadtxt(open("imdb_prodco_class.txt"),dtype=str,skiprows=0)
#ff=open('yh_count.txt','w')#6
for jj in range(1):
    zl = 0
    sum = 0
    train_data = []
    valid_data = []
    # 每个类按比例抽取
    my_matrix = np.loadtxt(open("imdb_prodco_class.txt"), dtype=str, skiprows=0)
    X, y = my_matrix[:,:-1],my_matrix[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)#测试集比例哦
    train_data = np.column_stack((X_train, y_train))
    valid_data = np.column_stack((X_test, y_test))

    c1 = 0
    print(jj)
    c2 = 0
    count = 0
    #for j_tr in train_data:
        #k=j_tr[0]
        #w1.write(str(k) + " " + str(node_c[k]) + " " + str(node_num[k]) + "\n")
    #for j_tr in valid_data:
    #    k = j_tr[0]
    #    w2.write(str(k) + " " + str(node_c[k]) + " " + str(node_num[k]) + "\n")
    for j_fa in valid_data:  # 具体哪个node
        class_end = ""
        class_p = 1
        for key in class_cl:  # 每个节点对每一类的P值
            kin = 0
            kout = 0
            D_s = 0
            Ds = 0
            j=j_fa[0]
            asso = node_n[j]
            for i in asso:
                #tt.write(node_c[i]+" ")
                if i in valid_data:
                    kout = kout + 1
                else:
                    if node_c[i] == key:
                        kin = kin + 1
                    else:
                        kout = kout + 1
            #tt.write(" \n")
            for k in valid_data:
                k = k[0]
                D_s = int(node_num[k]) + D_s
            for k in train_data:
                k = k[0]
                cla = node_c[k]
                if cla == key:
                    Ds = int(node_num[k]) + Ds

                else:
                    D_s = int(node_num[k]) + D_s
            pvalue=jc(kin,kout,D_s,Ds)
            #tt.write(node_c[j]+"\n")
            #tt.write(j + " " + key + " " + str(kin) + " " + str(kout) + " " + str(Ds) + " " + str(D_s) + " " + str(
             #   pvalue) + "\n")
            #tt.write(str(asso)+"\n")
            if pvalue < class_p:
                class_p = pvalue
                class_end = key
       # tt.write("\n")
        sum = sum + 1
        if node_c[j] == class_end:
            zl = zl + 1

    print(zl/sum)
    accu=accu+zl/sum
    #ff.write(str(c1) +" "+str(c2)+ " " + str(count) + " 4240 " +str(zl/sum)+"\n")
print(sum)
print(zl)
print(accu/30)
