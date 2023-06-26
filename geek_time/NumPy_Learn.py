import numpy as np
#Numpy数组和Python列表性能对比：
#比如我们想要对一个Numpy数组和Python列表中的每个数进行求平方。那么代码如下：

# Python列表的方式
import time
time1 = time.time()
array = []
for d in range(100000):
    array.append(d**2)
time2 = time.time()
use_time = time2 - time1
print(use_time)
#结果为：0.04330182075500488

time3 = time.time()
n = np.arange(100000)**2
time4 = time.time()
print(time4-time3)
#结果为：0.0013949871063232422
