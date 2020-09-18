x = int(input('请输入一个不超过1000的数字:'))
fac=[]
for i in range(2, x+1):
    while True:
        if x%i == 0:
            fac.append(i)
            x/=i
        else:
            break
#print
flag = 0
for i in fac:
    if flag == 0:
        print(i, end=' ')
        flag = 1
    else:
        print('*',i, end=' ')
