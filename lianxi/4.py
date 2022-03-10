"""
    水仙花数
# """
for x in range(100, 1000):
    baiwei = x // 100
    shiwei = x // 10 - baiwei * 10
    gewei = x - baiwei * 100 - shiwei * 10
    if baiwei**3 + shiwei**3 + gewei**3 == x:
        print(f"{x}为水仙花数！")

# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)
"""
    正整数反转
"""
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
"""
    斐波那契数列
"""
# a = 0
# b = 1
# for i in range(1, 100):
#     a, b = b, a + b
#     print(a, end="   ")
a = 0
b = 1
print(b)
for i in range(11):
    c = a + b
    a = b
    b = c
    print(c)

