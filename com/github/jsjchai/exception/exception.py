#!/usr/bin/python3

# 除零异常
try:
  a = 1 / 0
except ZeroDivisionError:
  print("In addition to the zero abnormal")

# 抛出异常
try:
  num = 1 / 0
except ZeroDivisionError:
  raise NameError('In addition to the zero abnormal')
