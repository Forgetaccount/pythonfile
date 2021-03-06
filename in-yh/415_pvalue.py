from sklearn.model_selection import KFold
import math

accu = 0
for jj in range(30):
    zl = 0
    sum = 0
    f = open('industry_yh_node_num_n.txt', 'r')  # 1
    node_num = {}  # node---num
    node_n = {}  # node---asso
    for line in f.readlines():
        line = line.strip()
        s = line.split()
        x = s[0]
        pinjie = s
        node_num[s[0]] = s[1]
        del (pinjie[0])
        del (pinjie[0])
        node_n[x] = pinjie
    f.close()

    f1 = open('industry_yh_class.txt', 'r')  # 2
    node_c = {}  # node---class
    c_num = {}  # node-----num0--2188
    num_c = {}  # 所有数字对应node  num0-2188----node
    ll = 0
    for l in f1.readlines():
        line = l.strip()
        s = line.split()
        node_c[s[0]] = s[1]
        c_num[s[0]] = ll
        num_c[ll] = s[0]
        ll = ll + 1

    class_cl = ['Transportation', 'Services', 'Healthcare', 'Financial', 'Energy', 'BasicMaterials',
                'CapitalGoods', 'ConsumerCyclical', 'Utilities', 'Technology', 'ConsumerNonCyclical',
                'Conglomerates']  # 3
    D = 28292  # 4

    f2 = open('fac1.txt', 'r')  # 5
    fac = {}
    for line in f2.readlines():
        line = line.strip()
        s = line.split()
        fac[int(s[0])] = float(s[1])
    f2.close()

    jj = 0



    def jc(kin, kout, D_s, Ds):
        ki = kin + kout
        x = fac[Ds]
        y = fac[D_s - ki]
        xx = fac[ki]
        yy = fac[D - 2 * ki]
        z = fac[D - ki]
        if kin == 0:
            u1 = 1
        else:
            u1 = fac[kin]
        if kout == 0:
            u2 = 1
        else:
            u2 = fac[kout]
        u3 = fac[Ds - kin]
        u4 = fac[D_s - ki - kout]
        p = x + y + yy + xx
        q = u1 + u2 + u3 + u4 + z
        qi = kout * (Ds - kin) / (kin * (D_s - kout))
        # print((1 - math.pow(qi, kout + 1)) / (1 - qi))
        right = (1 - math.pow(qi, kout + 1)) / (1 - qi)
        pvalue = math.exp(p - q) * right
        return pvalue


    ff = open('yh_count.txt', 'w')  # 6
    train_data = []
    valid_data = []
    # 每个类按比例抽取
    for c in class_cl:
        list_class = []
        class_dict = {}  # 数字对应node的字典
        i = 0
        ii = 0
        for i in range(1798):  # 7 实体的个数-1  0--1440
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
    c1 = 0
    print(jj)
    c2 = 0
    count = 0
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
            if kin == 0 & kout == 0:
                c1 = c1 + 1
                ff.write(j + " 000 " + "\n")
                continue
            else:
                count = count + 1

            # ki = kin + kout
            for k in valid_data:
                D_s = int(node_num[k]) + D_s
            for k in train_data:
                cla = node_c[k]
                if cla == key:
                    Ds = int(node_num[k]) + Ds

                else:
                    D_s = int(node_num[k]) + D_s
            pvalue = jc(kin, kout, D_s, Ds)
            ff.write(j + " pva " + "\n")
            if pvalue < class_p:
                class_p = pvalue
                class_end = key
        sum = sum + 1
        if count == 0:
            c2 = c2 + 1
            continue

        if node_c[j] == class_end:
            zl = zl + 1

    print(zl / sum)
    accu = accu + zl / sum

print(sum)
print(zl)
print(accu/30)