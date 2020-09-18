import random
y=[random.randint(1,100) for i in range(1000)]
z=set(y)
for i in z:
    print(i,'出现次数:',y.count(i))
