#!/usr/bin/python3

class A:
  def print(self):
    print("A")

class B(A):
  def print(self):
    print("B")

class C:
  def print(self):
    print("C")

class D(A,C) :
  def print(self):
    print("D")

a = A()
print(a.print())

a = B()
print(a.print())

a = D()
print(a.print())