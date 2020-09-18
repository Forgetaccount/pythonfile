import numpy as np
#np.random.seed(0)
#p = np.array([0.1, 0.0, 0.7, 0.2])
class_cl=['a','b','c','d']
asso=['a','c','d','a','a','a','a','a','a','c']

pbb={}
for j in class_cl:
    pbb[j] = 0
q = []
for j in asso:

    for c in cl:
        if j == c:
            num[c] = num[c] + 1

for c in cl:
    q.append((num[c]) / 10)

n1 = float(q[0])
n2 = float(q[1])
n3 = float(q[2])
n4 = float(q[3])
# p=np.array( num.keys())
p = np.array([n1, n2, n3, n4])
index = np.random.choice(cl, p=p.ravel())
n8 = float(q[7])
n9 = float(q[8])
            n10 = float(q[9])
            n11= float(q[10])
            n12= float(q[11])
            n13 = float(q[12])