import numpy as np
from sklearn.model_selection import train_test_split
import math
f1=open('cora_cite_class.txt','r')
class_cl=['ProbabilisticMethods','Theory','CaseBased','NeuralNetworks','GeneticAlgorithms'
    ,'RuleLearning','ReinforcementLearning']#3

node_c={}
num_c={}
k=0
for line in f1.readlines():
    line=line.strip()
    s=line.split(" ")
    node_c[s[0]]=s[1]
    num_c[k]=s[0]
    k=k+1
class_dict={}
train_data=[]
valid_data=[]
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
            # v5.write(str(ii) + " " + no + " " + node_c[no] + " " + node_num[no] + "\n")
            ii = ii + 1
    print(len(list_class))
    train,valid=train_test_split(list_class,test_size=0.3)
    for x in train:
        train_data.append(x)
    for y in valid:
        valid_data.append(y)
    print(len(train))





xx=open('111.txt','w')
yy=open('222.txt','w')
for a in train_data:
    xx.write(str(a)+" "+node_c[a]+"\n")
for a in valid_data:
    yy.write(str(a)+" "+node_c[a]+"\n")












