
a={}
f=open('w2.txt','r')
f1=open('w3.txt','r')
for line in f1.readlines():
    line = line.strip()
    s = line.split()
    a[s[1]]=1
for line in f.readlines():
    line = line.strip()
    s = line.split()
    a[s[1]]=1
print(len(a))






