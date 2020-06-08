# -*- coding:utf-8 -*-
# @Description:分隔字符
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import datetime
my_date = datetime.date(2020, 6, 3)
print(my_date)
print(my_date.weekday())
# 字符串中的分隔符是什么，使用split时括号里用相同分隔符；如果字符串用空格分隔，那就不需要再括号里填分隔符
text = 'geeks-for-geeks'
# splits at space
word = text.split('-')
print(word)

text1 = 'geeks, for geeks'
# splits at space
word1 = text1.split()
print(word1)

text2 = 'geeks:for:geeks'
# splits at space
word2 = text2.split(':')
print(word2)

# insert and append

li = [1,2,3,4,5,]
li.append(234)
print(li)

li2 = [3,4,6,78]
li2.insert(1, 765)
print(li2)