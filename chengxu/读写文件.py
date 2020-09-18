file = open("example.txt","r",encoding='UTF-8')
content = file.read()
content=content.swapcase()#swapcase() 方法用于对字符串的大小写字母进行转换
print(content)
file = open("result.txt","w")
file.write(content)
file.close()
