# 计算平均成绩
# def main():
#     numbers=int(input("请输入学生人数："))
#     name=[None]*numbers
#     scores=[None]*numbers

#     for index in range(len(name)):
#         name[index] = input("请输入第%d个学生的姓名：" % (index+1))
#         scores[index] = float(input("请输入第%d个学生的成绩：" % (index+1)))
#     sum=0
#     for index1 in range(len(name)):
#         print(name[index1],":",scores[index1],"分")
#         sum=sum+scores[index1]
#     print("平均成绩是：",sum/numbers)

# if __name__ == "__main__":
#     main()

# 字典定义和使用

#######################################################################

# def dice1():
#     di = {"linyafei": 90, "sakura": 89, "wangwang": 97}
#     for index in di:
#         print("%s的成绩是：%d" % (index, di[index]))
#     di["wangwang"] = 66
#     di["lin"] = 100
#     di.update(xi=89, liu=78)
#     print(di)
#     print(di.get("lin"))

#     #这句话是如果没有“lin”这个关键字，则默认值是110
#     print(di.get("lin", 110))

#     # Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。
#     print(di.popitem())

#     #     key: 要删除的键值
#     # default: 如果没有 key，返回 default 值
#     print(di.pop("sakura", 110))
#     di.clear()
#     print(di)

######################################################################

# def sakura():
#     stu = {"name": "张三", "age": 17, "tel": 1899999999}
#     print(stu)
#     print(stu.keys())
#     print(stu.values())
#     print(stu.items())
#     for elem in stu:
#         print(elem)
#         # name
#         # n a
#         # age
#         # a g
#         # tel
#         # t e
#         print(elem[0], elem[1])

# if __name__ == "__main__":
#     sakura()

#################################################

# def sakura():
#     # 用range生成数值列表
#     list1 = list(range(0, 11))
#     print(list1)
#     # 将m和n里的数据逐个取出
#     list2 = [m + n for m in "ABCDEF" for n in "123456"]
#     print(list2)
#     list3 = (x + y for x in "XYZ" for y in "890")
#     for itme in list3:
#         print(itme)

# if __name__ == "__main__":
#     sakura()

# refs = [x for x in range(1, 34)]
# print(refs)

# d = {'xiaobai': 20, 'lisa': 18, 'daidi': 21, 'yujiemeigui': 22}
# d1 = {'x': 1, 'y': 2}
# d2 = d.update(d1)
# print(d2)  # 返回值为None
# print(d)  # 查看原字典

# names = ["sakura", "lin", "wang", "zhang"]
# subs = ["语", "数", "外"]
# cj = [[0] * 3] * 4

# for row, name in enumerate(names):

#     for col, sub in enumerate(subs):
#         print("%s的%s成绩是：" % (name, sub))
#         cj[row][col] = float(input())

# print(cj)

