#!/usr/bin/python3

str = "hello,python"

# 输出第一个到倒数第二个的所有字符
print(str[0:-1])
# 输出第三个以后所有字符
print(str[2:])
# 输出字符串三次
print((str + " ") * 3)
# 截取
print(str[5])

# 字符串不能改变
str[5] = "#"
print(str[5])
