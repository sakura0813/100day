#带参数的函数

def sakura(a,b,c):
    return a+b+c

print(sakura(1,2,3))

#可变参数

def sakura1(*args):
    sum=0
    for num in args:
        sum=num+sum
    return sum

num1=[1,2,3,4,5,6]
#如果想让数组逐个被读取，需要在调用函数时，在数组前面加上*
print(sakura1(*num1))

#关键字参数

def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)

#最后一个参数需要一个变量盛放
person("林亚飞",25,tel="186333333")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 关键字参数:**kw
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Frank','37')
person('Frank','37',city='Shanghai')
person('Frank','37',gender='M',job='Engineer')