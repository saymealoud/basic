import matplotlib.pyplot as plt
A_score = [10, 15, 20, 12, 17, 10, 30, 35, 18, 4]
B_score = [25, 11, 21, 32, 22, 32, 12, 5, 3, 25]
score_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fig=plt.figure()
#初始化绘图区域
ax=fig.add_axes([0,0,1,1])
ax.scatter(score_range, A_score, color='y',label="A_score")
ax.scatter(score_range, B_score, color='b',label="B_score")
ax.set_xlabel('Score Range') #设置x轴的表达含义
ax.set_ylabel('Team Scored') #设置Y轴的表达含义
ax.set_title('scatter plot') #设置标题
#设置图例
plt.legend()
plt.show()