import matplotlib.pyplot as plt
#初始图形对象
fig = plt.figure()
#添加子图区域，其中的参数值含义是[left, bottom, width, height ]
#例如[0.1, 0.1, 0.8, 0.8]，表示从画布 10% 的位置开始绘制, 宽高是画布的 80%。
#我们常用的初始化值是[0,0,1,1]其代表的含义从左上角开始，宽高都是画布的100%
ax = fig.add_axes([0,0,1,1])
langs = ['football', 'tennis', 'basketball', 'ping-pong', 'volleyball']
students = [23,17,35,29,12]
#绘制柱状图
ax.bar(langs,students)
plt.show()