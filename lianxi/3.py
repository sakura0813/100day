"""
    计算1-100的和
"""
sum = 0
for x in range(101):
    sum = sum + x

print(f"100以内的整数和为：{sum}")
"""
    计算1-100的基数和
"""
sum_ji = 0
for x_ji in range(1, 100, 2):
    sum_ji = sum_ji + x_ji

print(f"1-100的基数和为：{sum_ji}")

"""
    输出九九乘法表
"""

for i in range(1, 10):
    print()
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}", end="\t")
