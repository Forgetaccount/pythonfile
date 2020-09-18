int_count=[]
up_count=[]
low_count=[]
other_count=[]
def number(a):
    for i in a:
        if i.isdigit():
            int_count.append(i)
        elif i.isupper():
            up_count.append(i)
        elif i.islower():
            low_count.append(i)
        else:
            other_count.append(i)
    return up_count,low_count,int_count,other_count
x=input('请输入一个字符串：')
a,b,c,d=number(x)
print('大写字母的个数：'+str(len(a)))
print('小写字母的个数：'+str(len(b)))
print('数字的个数：'+str(len(c)))
print('其他字符的个数：'+str(len(d)))
a=tuple(a)
b=tuple(b)
c=tuple(c)
d=tuple(d)
print(a,b,c,d)
