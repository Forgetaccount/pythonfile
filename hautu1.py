import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x_data = ['0.2','0.4','0.6','0.8']
y_data = [0.5848,0.6913,0.7378,0.789]
y_data2 = [0.8029,0.8064,0.8082,0.811]
y_data3=[0.7556,0.7785,0.7916,0.807]
y_data4=[0.77145,0.7773,0.7924,0.7971]
y_data5=[0.7874,0.8058,0.8138,0.82]
plt.plot(x_data,y_data,color='red',label='Initialize_Method1',linewidth=2.0,linestyle='--')
plt.plot(x_data,y_data2,color='blue',label='Initialize_Method2',linewidth=2.0,linestyle='--')
plt.plot(x_data,y_data3,color='green',label='Initialize_Method3',linewidth=2.0,linestyle='--')
plt.plot(x_data,y_data4,color='black',label='Initialize_Method4',linewidth=2.0,linestyle='--')
plt.plot(x_data,y_data5,color='orange',label='wvRN',linewidth=2.0,linestyle='-.')
plt.title('不同初始化方法的分类效果比较')
plt.xlabel('训练集比例')
plt.ylabel('准确率')
plt.legend(loc=0,ncol=2)
plt.show()
