"""
    函数参数问题
"""


def add(a=1, b=1, c=1):
    res = a + b + c
    return res


# 调用函数
# 只传递一个参数，后面的参数默认,  =15+1+1
res1 = add(15)

# 只传递两个函数，后面的参数默认,  =11+12+1
res2 = add(11, 12)

print(f"res1={res1},res2={res2}")


# 可变参数,求和
def Add(*args):
    total = 0
    for num in args:
        total = total + num
    return total


# 调用函数
fa = Add(2, 3, 1, 4, 5, 6, 444)
print(fa)

# 判断数字是否为回文数


def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


res = is_palindrome(12321)
print(res)
