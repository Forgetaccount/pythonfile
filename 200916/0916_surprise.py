from sklearn.model_selection import train_test_split
import math
import numpy as np
f=open('cora_wuguli.txt','r')
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
f1=open('cora_class_num.txt','r')
node_c=np.zeros((3583,2))#node---class

c_num={}#node-----num0--2188
num_c={}#所有数字对应node  num0-2188----node
ll=0
i=0
data=[]
node_class={}
for l in f1.readlines():
    line=l.strip()
    s=line.split()
    node_c[i,0]=s[0]
    node_c[i,1]=s[1]
    node_c[s[0]] = s[1]
    data.append(s[0])
    i=i+1
    c_num[s[0]]=ll
    num_c[ll] = s[0]
    ll=ll+1

class_cl=[1,2,3,4,5,6,7]
#['1','2','3','4','5','6','7']
#['ProbabilisticMethods','Theory','CaseBased','NeuralNetworks','GeneticAlgorithms'
    #,'RuleLearning','ReinforcementLearning']
index=node_c[:,1]==2
print(len(node_c[index]))

train_data = []
valid_data = []
train_data , valid_data = train_test_split(data, test_size=0.3)
#unk=valid_data[:,0]
print(train_data)
print(len(train_data))
print(len(valid_data))




































