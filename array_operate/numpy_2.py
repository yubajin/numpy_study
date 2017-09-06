import numpy as np


'''
a: 
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]

'''
a = np.arange(24).reshape(2,3,4)
# print('a:',a)
b = a[1][1][1]
# print('b:',b)


'''
c: 用:表示当前维度上所有下标
[[ 8  9 10 11]
 [20 21 22 23]]
'''
c = a[:,2,:]
# print('c:',c)


'''
d: 
[[ 1  5  9]
 [13 17 21]]
'''
d = a[:,:,1]
# print('d:',d)


'''
e: 用...表示没有明确指出的维度
[[ 1  5  9]
 [13 17 21]]
'''
e = a[...,1]
# print('e:',e)


'''
f:
[[ 5  6]
 [17 18]]
 '''
f = a[:,1,1:-1]
# print('f:',f)

'''
g1:[0 1 2 3],g2:[4 5 6 7],g3:[ 8  9 10 11]
'''
g1,g2,g3 = np.split(np.arange(12),3)
# print('g1:%s,g2:%s,g3:%s'%(g1,g2,g3))

'''
按照下标位置进行划分
[array([0, 1]), array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11]), array([12, 13, 14])]
'''
h = np.split(np.arange(15), [2, -3])
# print('h:',h)


# l0:
# [[0 1 2]
#  [3 4 5]]
# l1:
# [[ 6  7  8]
#  [ 9 10 11]]
l0 = np.arange(6).reshape((2, 3))
l1 = np.arange(6, 12).reshape((2, 3))
# print('l0:',l0)
# print('l1:',l1)

'''
vstack是指沿着纵轴拼接两个array，vertical
hstack是指沿着横轴拼接两个array，horizontal
更广义的拼接用concatenate实现，horizontal后的两句依次等效于vstack和hstack
stack不是拼接而是在输入array的基础上增加一个新的维度
'''
m = np.vstack((l0, l1))
p = np.hstack((l0, l1))
q = np.concatenate((l0, l1))
r = np.concatenate((l0, l1), axis=-1)
s = np.stack((l0, l1))

# print(p)
# print(r)
# print(s)

'''
按指定轴进行转置
array([[[ 0,  3],
        [ 6,  9]],

       [[ 1,  4],
        [ 7, 10]],

       [[ 2,  5],
        [ 8, 11]]])
'''
t = s.transpose((2, 0, 1))

'''
默认转置将维度倒序，对于2维就是横纵轴互换
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
'''
u = a[0].transpose()	# 或者u=a[0].T也是获得转置

'''
逆时针旋转90度，第二个参数是旋转次数
array([[ 3,  2,  1,  0],
       [ 7,  6,  5,  4],
       [11, 10,  9,  8]])
'''
v = np.rot90(u, 3)

'''
沿纵轴左右翻转
array([[ 8,  4,  0],
       [ 9,  5,  1],
       [10,  6,  2],
       [11,  7,  3]])
'''
w = np.fliplr(u)

'''
沿水平轴上下翻转
array([[ 3,  7, 11],
       [ 2,  6, 10],
       [ 1,  5,  9],
       [ 0,  4,  8]])
'''
x = np.flipud(u)

'''
按照一维顺序滚动位移
array([[11,  0,  4],
       [ 8,  1,  5],
       [ 9,  2,  6],
       [10,  3,  7]])
'''
y = np.roll(u, 1)

'''
按照指定轴滚动位移
array([[ 8,  0,  4],
       [ 9,  1,  5],
       [10,  2,  6],
       [11,  3,  7]])
'''
z = np.roll(u, 1, axis=1)