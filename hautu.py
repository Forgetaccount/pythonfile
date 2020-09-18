import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x_data = ['0.2','0.4','0.6','0.8']
y_data = [0.7782,0.8226,0.8445,0.85]
y_data2 = [0.81936,0.844,0.85349,0.861]
y_data3=[0.7807,0.8221,0.8436,0.8535]
y_data4=[0.7427,0.8054,0.8395,0.8495]
y_data5=[0.795,0.8319,0.85,0.856]
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
