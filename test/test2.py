import math

f1=open('train.txt')
f2=open('valid.txt')
f3=open('node_num_n.txt')
js=0
for line in f3.readlines():
    line=line.strip()
    s=line.split()
    if int(s[1])>4:
        js=js+1

print(js)
print("sss")
D=23332
Ds=0
D_s=0
dict1={}
dict2={}
for line in f1.readlines():
    line=line.strip()
    s=line.split()
    dict1[s[0]]=s[2]
    if s[1]=='Financial':   #key
        Ds=Ds+int(s[2])
    else:
        D_s=D_s+int(s[2])

for line in f2.readlines():
    line=line.strip()
    s=line.split()
    dict1[s[0]] = s[2]
    D_s=D_s+int(s[2])
sum=0

ki=8
kin=2
kout=6


f4 = open('fac1.txt', 'r')  # 4
fac = {}
for line in f4.readlines():
    line = line.strip()
    s = line.split()
    fac[int(s[0])] = float(s[1])
f4.close()
print(Ds)
print(D_s)
a=fac[Ds]
b=fac[D_s-ki]
c=fac[ki]
d=fac[D-2*ki]

u1=fac[kin]
u2=fac[kout]
u3=fac[Ds-kin]
u4=fac[D_s-ki-kout]
u5=fac[D-ki]
qi = kout * (Ds - kin) / (kin * (D_s - kout))
pvalue = (math.exp(a+b+c+d-u1-u2-u3-u4-u5) )* ((1 - math.pow(qi, kout + 1 ))/ (1 - qi))
print(pvalue)


