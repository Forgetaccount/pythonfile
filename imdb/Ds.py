
f1=open('w1.txt','r')
f2=open('w2.txt','r')
s1=0
s2=0
key="NOTblockBuster"
for line in f1.readlines():
    line = line.strip()
    s = line.split()
    if s[1]==key:
        s1=s1+int(s[2])
    else:
        s2=s2+int(s[2])
for line in f2.readlines():
    line = line.strip()
    s = line.split()
    s2=s2+int(s[2])
print(s1)#Ds
print(s2)#D_S




