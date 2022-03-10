import sys
"""
    转移字符“\\”
"""

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
"""
    如果不希望字符串中的`\`表示转义，
    我们可以通过在字符串的最前面加上字母`r`来加以说明
"""
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
"""
    列表list []
"""

# 定义列表
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_num)
lsit_str = ["hello world!"]
lsit_str1 = lsit_str * 3
print(lsit_str1)
print(len(lsit_str1))
print(list_num[1])
print(list_num[2])
print(list_num[-2])
list_num[2] = 10
print(list_num)
for num in list_num:
    print(num, end=" ")
for num in range(len(list_num)):
    print(list_num[num])

for key, value in enumerate(list_num):
    print(f"list_num_{key}={value}")
list_num.append(233)
list_num.insert(1, 3332)
print(list_num)

list_num1 = [45, 34, 23]
list_num.extend(list_num1)
list_num = list_num + [12, 32, 123]
print(list_num)
if 233 in list_num:
    list_num.remove(233)

print(list_num)
list_num.pop(0)
print(list_num)
list_num.clear()
print(list_num)

fruits = ["grape", "apple", "strawberrty", "waxberry"]
fruits = fruits + ["pitaya", "prar", "mango"]
fruits1 = fruits[1:4]
fruits2 = fruits[:4]
fruits3 = fruits[-3:-1]
fruits4 = fruits[::-1]
print(f"{fruits1},\n {fruits2},\n {fruits3},\n {fruits4}")

fruits5 = sorted(fruits)
fruits6 = sorted(fruits, reverse=True)
print(f"{fruits5},\n {fruits6}")

fruits7 = sorted(fruits, key=len, reverse=True)
print(fruits7)
"""
    生成器和生成式
"""

L = [x for x in range(0, 11)]
print(L)
str_hello = "hello"
num_123 = [1, 2, 3]
L = [(str_hello1, str_num1) for str_hello1 in str_hello
     for str_num1 in num_123]
print(L)
F = [x + y for x in "ABCD" for y in "12345"]
print(F)
f = [x**2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)

L11 = (x * x for x in range(1, 11))
print(L11)
print(next(L11))
print(next(L11))
print(next(L11))
for L in L11:
    print(L11)
L12 = (x * x for x in range(1, 11) if x % 2 == 0)
print(L12)
print(next(L12))
print(next(L12))
print(next(L12))
for L in L12:
    print(L12)
"""
    元组 ()
    元组不可以改变里面元素的值，但是列表可以，
    可以把元组转换成列表进行修改元素的值
"""

t = ("林亚飞", True, 25, "河南省")
print(t[0], t[3])
for yuanzu in t:
    print(yuanzu)

person = list(t)
print(person[1], person[2])
person[1] = False
print(person[1])
# 将列表转换成元组
person = tuple(person)
print(person)
"""
    集合 {}
"""

set1 = {1, 2, 3, 4, 5, 6}
print(set1)
# 集合的长度
print("length=", len(set1))

# 集合构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)

# 和列表类似，集合也有类似的语法
set4 = {(jihe1, jihe2) for jihe1 in range(0, 2) for jihe2 in range(20, 23)}
print(set4)

# 向集合中添加元素
set1.add(34)
# 向集合中添加元素只能用update
set2.update([11, 16])
# 删除指定索引位置的元素
set2.discard(5)
print(set1)
print(set2)

if 4 in set2:
    set2.remove(4)
print(set2)
# 删除集合元素第一个元素，执行成功返回1
print(set3.pop())
set3.pop()
print(set3)

# 集合的交并差运算
collect = set()
collect = {num for num in range(0, 11)}
collect1 = {num for num in range(0, 21)}
# 交集
print(collect & collect1)
# 并集
print(collect | collect1)
# 集合差运算
print(collect1 - collect)
# 返回不同的元素
print(collect ^ collect1)
# 返回布尔值 True
print(collect <= collect1)
# False
print(collect >= collect1)
"""
    字典的使用 "键" 和 "值"
"""

Age = {"sakura": 12, "林亚飞": 25, "白居易": 70}

print(Age)

# 字典的字面量语法

Number = dict(one=1, two=2, three=3)
print(Number["one"])
# 通过zip函数将两个序列压成字典
zip_1 = dict(zip(["a", "b", "c"], "123"))
print(zip_1)
# 字典的推导式语法,   冒号前是键，后面是值
dictionaray = {num: num**2 for num in range(1, 10)}
print(dictionaray)
Number.update(four=4, five=5)
print(Number)
if "four" in Number:
    print(Number["four"])
# 获取对应键的值
print(Number.get("four"))
# get()方法在字典里找对应的值，如果找不到返回默认值25
print(Number.get("linyafei", 25))
# 删除字典中最后一位元素
print(Number.popitem())
print(Number.popitem())
print(Number.pop("five", 10))
print(Number)
Number.clear()
print(Number)
