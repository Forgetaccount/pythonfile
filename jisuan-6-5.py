import math
import numpy
M=13
F=28
p=6
m=8
j=6
aa=0
for j in range(9):
    if j>5:
        print(j)
        a=math.factorial(M)*math.factorial(F-M)*math.factorial(m)*math.factorial(F-m)
        b=math.factorial(j)*math.factorial(M-j)*math.factorial(m-j)*math.factorial(F-M-m+j)*math.factorial(F)
#a=math.factorial(12)*math.factorial(16)*math.factorial(14)
#b=math.factorial(28)*math.factorial(2)*math.factorial(12)
 #print(-math.log(a/b,10))
        a3=a/b
        aa=aa+a3
c=-math.log(aa,10)
print(c)

d=p/m
f=M/F
k=m*(d*math.log(d/f)+(1-d)*math.log((1-d)/(1-f)))
#kk=math.factorial(17000000)
#kk=1672418*1672417*1672418*1672418*1672418*1672418*1672418*1672418*1672418*1672418
#kk=math.pow(19750000,20)
#kk=math.exp(20000/math.e,20000)
print(k)
#print(kk)
#for i in range(10000,14000000):
#    print(i)
#    kk=math.log(i,4000)
 #   print(kk)

a=numpy.zeros((3583,2))


