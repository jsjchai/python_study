#!/usr/bin/python3

import os

# 当前文件绝对路径
current_path = os.path.abspath(__file__)
# 当前文件目录
dir = os.path.dirname(current_path)

print("path:", current_path, "\ndir:", dir)

f = open(dir + "/1.txt", mode="r+", newline='')

f.write("\n123456")

line = f.readline()
while line:
  print(line)
  line = f.readline()
f.close()

print("------------")
for line in open("1.txt"):
  print(line)
