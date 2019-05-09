#!/usr/bin/python3

class User:

  # 定义基本属性
  name = ""
  age = -1
  # 定义私有属性
  _weight = -1

  # 定义构造方法
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def setWeight(self, weight):
    self._weight = weight

  def toString(self):
    print("name:%s,age:%d,weight:%f" % (self.name, self.age, self._weight))


# 实例化
u = User("tom", 19)
u.setWeight(45.5)
print(u)
print(u.toString())
