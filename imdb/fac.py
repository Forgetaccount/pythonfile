import math

kin=18
kout=13
Ds=18769
D_s=21865
ki=kin+kout
D=Ds+D_s
x=math.factorial(Ds-ki)
y=math.factorial(D_s)
z=math.factorial(ki)
a=math.factorial(D-2*ki)

i=math.factorial(D-ki)
j=math.factorial(kin)
k=math.factorial(kout)
m=math.factorial(Ds-kin)
n=math.factorial(D_s-kout-ki)

P=(x*y*z*a)/(i*j*k*m*n)# xyazijkmn 均为计算阶乘后的结果
q1=(kout*(Ds-kin))/(kin*(D_s-kout))
q=(1-math.pow(q1,(kout+1)))/(1-q1)

p=q*P
print(p)
