
def wenben(x):
    if 'i' in x:
        x = x.replace('i','I')
        return x
    else:
        return ("x中不存在i")

x = input("请输入文本：")
print(wenben(x))

