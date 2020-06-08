# -*- coding:utf-8 -*-
# @Description: class continue
# @Author: Shimin
# @Copyright
# @Version:0.0.1

# 在初始化方法内部定义属性--（在__init__方法内部使用self.属性名=属性的初始值）
class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值 (属性名自定义，随便取；属性的初始值是一个框架，在下方可以定义多个不同的属性）
        # self.name = "Tom"
        self.name = new_name
    # 定义一个method
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫"

# tom是一个全局变量
# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat("Tom")
print(tom.name)
# print(tom.name)
lazy_cat = Cat("大懒猫")
lazy_cat.eat()

class Employee:
    # class attributes  属于类的，不是属于实例（一个具体的员工属性）的
    raise_amount = 1.04
    num_of_emps = 0
    # first, last, pay 都是属于一个员工的具体属性（实例变量）
    def __init__(self, first, last, pay):
        # instance attributes
        self.yeahfirst = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # 定义一个instance method
    def fullname(self):
        return '{} {}'.format(emp_1.yeahfirst, emp_1.last)

    # def apply_raise(self):
    #     self.pay = int(self.pay * self.raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

Employee.set_raise_amount(1.05)

emp_1 = Employee('Shimin', 'Cheng', 70000)
emp_2 = Employee('Shiyu', 'Cheng', 120000)
print(emp_2.yeahfirst)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
print(emp_1.raise_amount)
# 返回的是不同的内容，emp_1返回的内容中不包含raise_amount
print(Employee.__dict__)
print(emp_1.__dict__)
print(Employee.num_of_emps)