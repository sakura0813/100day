"""
格式化输出

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# 和C#不一样，打印出的结果是：%d ** %d = %d (1, 2, 1)
print('%d ** %d = %d' , (a, b, a ** b))