"""
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""

import time
import shutil
import os

#截获当前时间戳
seconds = time.time()
print(seconds)
#获取当前时间
localtime = time.localtime(seconds)
print(localtime)
#年
print(localtime.tm_year)
#月
print(localtime.tm_mon)
#日
print(localtime.tm_mday)
#接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串
asctime = time.asctime(localtime)
print(asctime)
#格式化时间
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
#接收以时间元组，并返回以可读字符串表示的当地时间，格式由"2018-1-1"决定
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

#复制文件
shutil.copy('function4.py', 'sakura.py')
#这是mac 查权限的控制台命令
#os.system('ls -l')
os.system('attrib *.*')
#更改当前文件夹
# os.chdir('Day07')
#让程序调用cmd执行参数
os.system('attrib *.*')
#创建文件夹
os.mkdir('test')
