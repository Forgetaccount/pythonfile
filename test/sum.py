import  math
f1=open('yh_count.txt','r')
f2=open('yh_count11.txt','w')
x=0
node=0
flag=0
for line in f1.readlines():
    x=x+1
    line=line.strip()
    s=line.split()
    if x%12==0:
        f2.write(str(s[1])+"\n")
        continue
    elif x%12==1:
        f2.write(str(s[0]) +" "+str(s[1])+" ")
        continue
    else:
        f2.write(str(s[1]+" "))
        continue

print(node)