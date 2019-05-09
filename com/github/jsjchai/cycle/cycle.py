#!/usr/bin/python3

# 计算1到100的和
n = 100
sum = 0
i = 1
while i <= n:
  sum = sum + i
  i += 1

print("1 到 %d 之和为：%d " % (n, sum))

# while...esle
count = 0
while count <= 5:
  count = count + 1
else:
  print(count, " 大于或等于 5")

# 无限循环
# i = 1
# while (i): print("hell,python")
# while 1 == 1:
#   num = int(input("输入一个数字  :"))
#   print("你输入的数字是: ", num)

# for
arr = list(range(5))
print(arr)
for i in arr:
  if i == 3:
    pass
    print("pass i=", i)
  else:
    print(i)
