# -*- coding:utf-8 -*-
# @Description:试错练习
# @Author: Shimin
# @Copyright
# @Version:0.0.1
from pip._vendor.six import b
# import time as t
# print(t.localtime())
# print(t.time())
from time import*
print(time())
listExample = [1, 234, 43, 786, 978, 24, 245]
# for i in range(listExample):
#      print(i)                               # 'list' object cannot be interpreted as an integer
for i in range(len(listExample)):  # 此时i表示的是下标

    print(listExample[i])  # 不可以用()代替[]
print("列表中元素2为：", listExample[2])
print("列表中元素0为：", listExample[0])  # 列表中第一个元素称为元素0


def fun(a, b):
    c = (a + b) * b
    print(c)


fun(b=4, a=2)


def sale_car(price, color, brand, is_second_hand):
    print("price:", price,
          "\ncolor:", color,  # 加上\n是为了给输出的结果换行
          "\nbrand:", brand,
          "\nis_second_hand:", is_second_hand)


sale_car(122234, "blue", "BMW", True)


def fun():
    a = 10
    return a + 100


print(fun())

# global & local variable
APPLE = 100  # global variable
a = None


def fun():
    global a
    a = 20
    return a + 100  # a now is a local variable


print(APPLE)
print('a past =', a)
print(fun())
print("a now = ", a)

text = "this is my first line.\nthis is my second line\nthis is my last line"
my_file = open("my file.txt", "w")  # w means write
my_file.write(text)
my_file.close()
append_text = "\nthis is appended file."
my_file = open("my file.txt", "a")  # a means append
my_file.write(append_text)
my_file.close()

file = open("my file.txt", "r")
# content = file.read()
readlines = file.readlines()
# print(content)
print(readlines)  # 以列表的形式返回原输入的内容

# 迷惑教学内容，垃圾
# # class
# class Calculator:
#     name = 'Good calculator'
#     price = 25
#
#     def add(self, x, y):
#         print(self.name)
#         result = x + y
#         print(result)
#
#     def minus(self, x, y):
#         result = x - y
#         print(result)
#
#     def divide(self, x, y):
#         print(x / y)
#
#     def times(self, x, y):
#         print(x * y)

a_example = eval(input("请输入一个数字："))
if a_example == 1:
    print("this number is one")


# tuple / list
a_tuple = (1, 2, 3, 44, 5)          # 用小括号
a_list = [1, 23, 45, 436, 65]       # 用中括号
for index in range(len(a_list)):
    print('index = ', index, 'number in list = ', a_list[index])

for index in range(len(a_tuple)):
    print('index = ', index, 'number in tuple = ', a_tuple[index])

# dictionary 字典，用大括号{}

