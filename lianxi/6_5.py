"""
    文字跑马灯效果
"""
import os
import time
import random


def main():
    string = "北京欢迎您..."

    while True:
        os.system("cls")
        print(string)
        time.sleep(0.5)
        string = string[1:] + string[0]


"""
    产生验证码，包括大小写字母数字构成
"""


def code(Lenth_code):
    """
    生成验证码
    """
    string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for _ in range(0, Lenth_code):
        index = random.randint(0, len(string))
        code = code + string[index]

    print(code)


"""
    获取文件名后缀
"""


def str_suffix(filename, has_dot=False):
    index = filename.rfind(".")
    suffix = filename[index + 1:]
    if has_dot:
        suffix = "." + suffix
    print(suffix)


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


"""
    返回列表中最大和第二大的元素符号
"""


def Max_num(list_num):
    """
    找出数列中最大和第二大的数字
    """
    for index in range(0, len(list_num)):
        if list_num[index] < list_num[index]:
            list_num[index], list_num[index + 1] = list_num[index +
                                                            1], list_num[index]
    return list_num

if __name__ == "__main__":
    # main()
    # code(4)
    str_suffix("1.py")
    str_suffix("name.py", True)
    print(get_suffix("1.pptx"))
    print(get_suffix("1.pptx", True))
    print(Max_num([3,4,2,6,7,9,8,]))