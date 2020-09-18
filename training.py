import numpy as np
from sklearn.model_selection import train_test_split
import math
f1=open('cora_cite_class.txt','r')
class_cl=['ProbabilisticMethods','Theory','CaseBased','NeuralNetworks','GeneticAlgorithms'
    ,'RuleLearning','ReinforcementLearning']#3

node_c={}
num_c={}
k=0



xx=open('111.txt','r')
yy=open('222.txt','r')

dict={}
for line in xx.readlines():
    line=line.strip()
    s=line.split(" ")
    dict[s[0]]=1
for line in yy.readlines():
    line=line.strip()
    s=line.split(" ")
    dict[s[0]]=1
print(len(dict))









