#!/usr/bin/python3

import sys


# 生成器函数 - 斐波那契
def fibonacci(n):
  a = 0
  b = 1
  count = 0
  while True:
    if (count > n):
      break
    yield a
    a, b = b, a + b
    count += 1
    print(a, b, count)


# f 是一个迭代器，由生成器返回生成
f = fibonacci(10)

while True:
  try:
    print("f=", next(f), " ")
  except StopIteration:
    sys.exit()
