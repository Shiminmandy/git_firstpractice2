# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1

# # 使用try调试
# try:
#     # value = 8 / 3
#     value = 8 // 0
#     print(value)
# except:                   # 异常的捕获
#     print('error')
#     response = input('do you want to change the value:')
#     if response == 'y':
#         valueUpdated = input('please enter the updated value:')
#         print(eval(valueUpdated))
# else:
#     print('no error, the value is :', value)
# finally:
#     print('-' * 100)


# 使用set
char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
print((set(char_list)))
print(sorted(set(char_list)))
print(type(set(char_list)))

# dictionary
dict_example = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict_example["year"])

import pickle
# file = open('pickle_example.pickle', 'wb')
# pickle.dump(dict_example, file)             # 括号里面第一个是要保存的内容
# file.close()                                # 被存储的内容转化为字节流，使得内容被更安全地保存
any_name = open("pickle_example.pickle", "rb")
whatever_name = pickle.load(any_name)
print(whatever_name)
print(whatever_name["year"])