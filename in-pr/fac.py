import math

kin=7
kout=45
Ds=1346
D_s=21986
ki=kin+kout
D=Ds+D_s
x=math.factorial(D_s-ki)
y=math.factorial(Ds)
z=math.factorial(ki)
a=math.factorial(D-2*ki)

i=math.factorial(D-ki)
j=math.factorial(kin)
k=math.factorial(kout)
m=math.factorial(Ds-kin)
n=math.factorial(D_s-kout-ki)

P=(x*y*z*a)/(i*j*k*m*n)
print(P)
q1=(kout*(Ds-kin) )/(kin*(D_s-kout))
q=(  1-math.pow(q1,(kout+1)) )/(1-q1)
p=q*P
print(p)
