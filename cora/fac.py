import math

kin=3
kout=0
Ds=2459
D_s=20057
ki=kin+kout
D=Ds+D_s
x=math.factorial(D_s-ki)
y=math.factorial(Ds)
z=math.factorial(ki)
a=math.factorial(D-2*ki)

i=math.factorial(D-ki)
j=math.factorial(kin)
k=math.factorial(kout)
m=math.factorial(D_s-ki-kout)
n=math.factorial(Ds-kin)

P=(x*y*z*a)/(i*j*k*m*n)
print(P)
q1=(kout*(Ds-kin) )/(kin*(D_s-kout))
print(q1)
q=(  1-math.pow(q1,(kout+1)) )/(1-q1)
print(math.pow(q1,(kout+1)))
print(q)
p=q*P
print(p)
