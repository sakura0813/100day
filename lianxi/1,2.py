import math
"""
    华氏温度到摄氏温度
    摄氏温度到华氏温度
"""
tempe_type = int(input("华社温度->摄氏温度请选1，摄氏温度->华社温度请选2:"))

if tempe_type == 1:
    hua_tmpe = float(input("请输入华氏温度："))
    she_temp = (hua_tmpe - 32) / 1.8
    print(f"{hua_tmpe}华氏温度等于{she_temp}摄氏度")
elif tempe_type == 2:
    she_temp = float(input("请输入摄氏温度："))
    hua_tmpe = she_temp * 1.8 + 32
    print(f"{she_temp}摄氏温度等于{hua_tmpe}华氏温度")
else:
    print("请选择正确的数字！")


"""
    输入元的半径计算圆的周长面积
"""

cicle_type = int(input("请选择计算圆的面积（输入1）还是周长（输入2）："))
if cicle_type == 1:
    r = float(input("请输入圆的半径："))
    mianji = math.pi*r**2
    print(f"圆的面积是：{mianji}")
elif cicle_type == 2:
    r = float(input("请输入圆的半径："))
    zhouchang = 2*math.pi*r
    print(f"圆的周长是：{zhouchang}")

"""
    判断年份是不是闰年
"""
year = int(input("请输入年份："))

is_leep=(year%4==0 and year%100==0 ) or year%400==0)
print(is_leep)