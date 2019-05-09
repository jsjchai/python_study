#!/usr/bin/python3

# set无序的 不允许重复


num1 = {1, 2, 3, 4, 5, 6}

print(num1)

if 1 in num1:
  print("exist")
else:
  print("not exist")

# 集合运算
a = set("123456")
b = set("357")

print(a)
print(b)

# 差集
print("差集:", a - b)
# 交集
print("交集:", a & b)
# 并集
print("并集:", a | b)
# a 和 b 中不同时存在的元素
print("不同时存在的元素:", a ^ b)
