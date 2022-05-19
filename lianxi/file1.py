
from base64 import encode


def main():
    f=None
    try:
        f=open("sakura.txt","r",encode="utf-8")
        print(f.read())
    except FileNotFoundError:
        print("没找到文件~")
    except file