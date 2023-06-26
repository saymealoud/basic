import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
# >>>输出结果：
# b 1.0
# c 2.0
# d NaN
# a 0.0
# dtype: float64
#如果不设置index的情况，默认是从0开始的索引
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)
# >>>输出结果：
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object