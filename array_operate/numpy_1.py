import numpy as np

a = [1, 2, 3, 4]     	#
b = np.array(a)         	# array([1, 2, 3, 4])
type(b)                   	# <type 'numpy.ndarray'>

b.shape                   	# (4,)
b.argmax()               	# 3
b.max()                   	# 4
b.mean()                  	# 2.5

c = [[1, 2], [3, 4]]  	# 二维列表
d = np.array(c)         	# 二维numpy数组
d.shape                   	#shape[0]和shape[1]分别代表行和列的长度 (2, 2)
d.size                   	# 4
d.max(axis=0)            	# axis=0:求各column的最大值array([3, 4])
d.max(axis=1)            	# axis=1:求各row的最大值array([2, 4])
d.mean(axis=0)          	# 找维度0，也就是第一个维度上的均值，array([ 2.,  3.])
d.flatten()              	# 展开一个numpy数组为1维数组，array([1, 2, 3, 4])
np.ravel(c)               # 展开一个可以解析的结构为1维数组，array([1, 2, 3, 4])

# 3x3的浮点型2维数组，并且初始化所有元素值为1
e = np.ones((3, 3), dtype=np.float)
# print(e.shape)
# print(e)

# 创建一个一维数组，元素值是把3重复4次，array([3, 3, 3, 3])
f = np.repeat(3, 4)
# print(f.shape)
# print(f)

# 2x2x3的无符号8位整型3维数组，并且初始化所有元素值为0
# [[[0 0 0]
#   [0 0 0]]
#
#  [[0 0 0]
#   [0 0 0]]]
g = np.zeros((2, 2, 3), dtype=np.uint8)
# print('g:',g)
# print('g.shape:',g.shape)                    # (2, 2, 3)
h = g.astype(np.float)  # 用另一种类型表示
# print(h)

l = np.arange(10)      	# 类似range，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
m = np.linspace(0, 6, 5)# 等差数列，0到6之间5个取值，array([ 0., 1.5, 3., 4.5, 6.])
print('l:',l)
print('m:',m)

p = np.array(
    [[1, 2, 3, 4],
     [5, 6, 7, 8]]
)
# print(p)

np.save('p.npy', p)     # 保存到文件
q = np.load('p.npy')    # 从文件读取