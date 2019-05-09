#!/usr/bin/python3

a1 = [1, 'a', 2, 'b', 3, 5.5]
a2 = [99, 100]

print(a1)
print(a1[3])
print(a1[3:])
print(a1[3:5])
print(a1 * 2)
print(a1 + a2)

a1[3:5] = []
print(a1)
