"""
函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 将求阶乘的功能封装成一个函数
# def factorial(n):
#     result = 1
#     for num in range(1, n + 1):
#         result *= num
#     return result


# print(factorial(7) // factorial(3) // factorial(4))

c=0

def functa(sakura):
    for i in range(0,sakura):
        
        #此处的c为全局变量，虽然在全局已经声明了全局变量c，
        #但是在函数里对c赋值会使c成为函数的局部变量，所以还要再函数里声明global c

        global c
        c=c+i
    return c



print(functa(101))