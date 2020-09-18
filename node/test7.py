from sklearn.model_selection import KFold
import math
f=open('node_num_n.txt','r')
sum=0
map={}
for line in f.readlines():
    line=line.strip()
    s=line.split()
    x=int(s[1])
    sum=sum+x
    map[s[0]]=0
f.close()
print(sum)
print(len(map))


