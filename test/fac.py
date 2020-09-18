import math
#算度数，最大度数的log
f1=open('fac0.txt','w')
su=1
f={}
fac=1

for fac in range(1,92249):
    print(fac)
    su=fac*su
    #f[fac]=su
    a=math.log(su)
    f1.write(str(fac))
    f1.write(" ")
    f1.write(str(a))
    f1.write("\n")
f1.close()

#n=3
#x=math.sqrt(2*math.pi*n) *math.pow(n/math.exp(1),n)
#x=0.5*math.log(2*math.pi*n,10)+n*math.log(n/math.exp(1),10)
#y=math.exp(1)   40634
#y=math.log(100,10)
#y=math.log(100,10)
#print(y)
#print(x)
'''
f2=open('fac1.txt','r')
fac={}
fac[0]=1
for line in f2.readlines():
    line=line.strip()
    s=line.split()
    fac[int(s[0])]=float(s[1])
f2.close()

#a=math.exp(fac[1000])
#print(math.exp(fac[23332]))
z=math.pow(2,3)
print(z)
x=10
a=math.log(math.e)
b=math.exp(a)
print(a)
print(b)
'''