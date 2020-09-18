
f2=open('WebKB-washington-link1.rn','r')
f1=open('WebKB-washington-cocite.rn','r')
a={}
for l in f1.readlines():
    line=l.strip()
    s=line.split(",")
    x=s[0]+","+s[1]
    a[x]=1
print(len(a))
sum=0
for l in f2.readlines():
    line=l.strip()
    s=line.split(",")
    x=s[0]+","+s[1]
    y=s[1]+","+s[0]
    if x in a:
        sum=sum+1
    elif y in a:
        sum=sum+1
print(sum)




