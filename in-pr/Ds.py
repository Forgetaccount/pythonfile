


class_cl=['Technology','Healthcare','Financial','Energy','BasicMaterials',
          'CapitalGoods','Utilities','ConsumerNonCyclical','Transportation',
          'Conglomerates','ConsumerCyclical','Services']
for key in class_cl:
    f1 = open('w3.txt', 'r')
    f2 = open('w2.txt', 'r')
    s1 = 0
    s2 = 0
    print(key)
    for line in f1.readlines():
        line = line.strip()
        s = line.split()
        if s[2] == key:
            s1 = s1 + int(s[3])
        else:
            s2 = s2 + int(s[3])
    for line in f2.readlines():
        line = line.strip()
        s = line.split()
        s2 = s2 + int(s[3])
    print(s1)  # Ds
    print(s2)  # D_S
    f1.close()
    f2.close()





