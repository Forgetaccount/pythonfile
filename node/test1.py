from sklearn.model_selection import KFold
import math

#建立字典 node_n  node_num
f=open('node_num_n.txt','r')
node_num={}
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
k=node_num['VSH']
kk=node_n['VSH']
#dict
f1=open('node_class.txt','r')
node_c={}
list=[]
c_num={}
num_c={}
ll=0
for l in f1.readlines():
    line=l.strip()
    s=line.split()
    list.append(s[0])
    node_c[s[0]]=s[1]
    c_num[s[0]]=ll
    num_c[ll] = s[0]
    ll=ll+1
kf = KFold(n_splits=5, shuffle=True)
key='CapitalGoods'

pp=open('pvalue.txt','w')
pp1=open('valid.txt','w')

accu=0
accu1=0
rec=0
rec1=0
pre=0
pre1=0
f=0
f1=0
for train, valid in kf.split(node_c):
    #print(train,valid)
    Ds=0
    D_s=0
    sear=[]
    for j in valid:
        sear.append(j)
        pp2 = num_c[j]
        pp1.write(str(j))
        pp1.write(" " + pp2 + "\n")
    print(sear)
    for j in train:#17
        yuansu = list[j]#ACAS
        cla = node_c[yuansu]#Financial
        if cla==key:
            if j in sear :
                print("hhh")
                D_s = int(node_num[yuansu]) + D_s
            else:
                Ds = int(node_num[yuansu]) + Ds
        else:
            D_s=int(node_num[yuansu])+D_s
   # print(D_s)
   # print(Ds)
    for j in valid:
        yuansu=list[j]
        D_s = int(node_num[yuansu]) + D_s
    j=0
    TP=0
    FP=0
    FN=0
    TN=0


    D = math.factorial(23332)
    for k in valid:
        j=j+1
        #print(j)
        #print(k)
        kin=0
        kout=0
        yuansu = list[k]
        #print(yuansu)
        asso=node_n[yuansu]
        for i in asso:
            c_n=c_num[i]
            if c_n in sear:
                kout = kout + 1
            else:
                if node_c[i] == key:
                    kin = kin + 1
                else:
                    kout = kout + 1

        #if kin==0:
        #    pp.write(yuansu + " " + str(0) + "\n")
        #    continue

        ki=kin+kout
        x=math.factorial(Ds)
        y=math.factorial(D_s-ki)
        xx=math.factorial(ki)
        yy = math.factorial(23332 - 2 * ki)

        z=math.factorial(23332-ki)
        u1=math.factorial(kin)
        u2=math.factorial(kout)
        u3=math.factorial(Ds-kin)
        u4=math.factorial(D_s-ki-kout)
        p=x*y*yy*xx
        q=u1*u2*u3*u4*z
        pvalue=p/q
        if pvalue<0.05:
            if node_c[yuansu]==key:
                TP=TP+1
                pp.write(yuansu + " " + "TP" + "\n")
            else:
                FP=FP+1
            pp.write(yuansu+" "+"FP"+"\n")
        else:
            if node_c[yuansu] == key:
                FN=FN+1
                pp.write(yuansu + " " + "FN" + "\n")
            else:
                TN=TN+1
            pp.write(yuansu+" "+"TN"+"\n")
        #pp.write(yuansu+" "+ str(pvalue)+"\n")
    zl=TP+TN
    zf=TP+TN+FP+FN
    r=TP/(TP+FN)
    p=TP/(TP+FP)
    print(zl)
    print("待分类节点:accu rec pre")
    print(zl/zf)
    print(r)
    print(p)
    f=f+2*p*r/(p+r)
    print(f)
    #break
    accu1=accu1+(zl/zf)
    rec1=rec1+r
    pre1=pre1+p
    for k in train:
        #print(j)
        j = j + 1
        kin = 0
        kout = 0
        yuansu = list[k]
        # print(yuansu)
        asso = node_n[yuansu]
        for i in asso:
            c_n = c_num[i]
            if c_n in sear:
                kout = kout + 1
            else:
                if node_c[i] == key:
                    kin = kin + 1
                else:
                    kout = kout + 1

        ki = kin + kout
        x = math.factorial(Ds-ki)
        y = math.factorial(D_s)
        xx = math.factorial(ki)
        yy = math.factorial(23332 - 2 * ki)
        x1= math.factorial(Ds)
        y1=math.factorial(D_s-ki)
        p3=x1*y1*xx*yy
        z = math.factorial(23332 - ki)
        u1 = math.factorial(kin)
        u2 = math.factorial(kout)
        u3 = math.factorial(Ds - kin-ki)
        u4 = math.factorial(D_s - kout)
        u5=math.factorial(Ds-kin)
        u6=math.factorial(D_s-ki-kout)
        q3=u5*u6*z*u1*u2
        p = x * y * yy * xx
        q = u1 * u2 * u3 * u4 * z
        if node_c[yuansu] == key:
            pvalue = p / q
        else:
            pvalue=p3/q3
        if pvalue < 0.05:
            if node_c[yuansu] == key:
                TP = TP + 1
            else:
                FP = FP + 1
            pp.write(yuansu + " " + key + "\n")
        else:
            if node_c[yuansu] == key:
                FN = FN + 1
            else:
                TN = TN + 1
            pp.write(yuansu + " " + "false" + "\n")
    zl = TP + TN
    zf = TP + TN + FP + FN
    r = TP / (TP + FN)
    p = TP / (TP + FP)
    print(zl)
    print("所有节点:accu rec pre")
    print(zl / zf)
    print(r)
    print(p)
    f1=f1+2 * p * r / (p + r)
    print(f1)
    # break
    accu = accu + (zl / zf)
    rec = rec + r
    pre = pre + p

print("\n")
print(accu/5)
print(rec/5)
print(pre/5)
print(f1/5)

print(accu1/5)
print(rec1/5)
print(pre1/5)
print(f/5)



