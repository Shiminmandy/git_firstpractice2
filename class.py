# -*- coding:utf-8 -*-
# @Description:关于class的开始与深入
# @Author: Shimin
# @Copyright
# @Version:0.0.1

# 定义只包含方法的类
# 动词一般为方法
# class 类名(大驼峰命名法，每个单词开头大写）:
# def method1(方法1)(self,参数列表):
# def method2(方法2)(self,参数列表):
# 创建对象-当一个类定义完之后，要使用这个类来创建对象
# 对象变量 = 类名()
# 初始化方法：__int__(专门用来定义一个类具有哪些属性的方法)
# example 1
class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
# 内部增加属姓名：可以使用  .属性名 利用赋值语句就可以了
# tom.name = "Tom"  # 不推荐使用，这种方式没有针对类（class）的代码进行修改，没有把对象的属性封装在类的内部

# 调用类中封装的方法
tom.eat()
tom.drink()
print(tom)               # <__main__.Cat object at 0x00000192FF1DB610> 当前创建的猫对象在内存中的16进制地址

# 转换地址
# addr = id(tom)
# print("%d" % addr)     # %d 以10进制输出数字
# print("%x" % addr)     # %x 以16进制输出数字

# 再创建一个猫对象
lazy_cat = Cat()
# 增加属性姓名
# lazy_cat.name = "大懒猫"
# lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)          # 内存地址不一样（使用相同的类，可以创建很多不同的对象）
