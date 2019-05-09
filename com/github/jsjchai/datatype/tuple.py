#!/usr/bin/python3

tuple = (1, 2, 3, 'a', 'b', 'c')
a = ('x', 'y', 'z')

print(tuple)
print(tuple[1:])
print(tuple[1:2])
print(tuple * 2)
print(tuple + a)

# 元组类型不支持修改
tuple[5] = 'aa'
print(tuple[5])

# 空元组
tup1 = ()
# 一个元素，需要在元素后添加逗号
tup2 = (1,)
