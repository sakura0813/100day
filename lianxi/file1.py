
from base64 import encode


def main():
    f=None
    try:
        f=open("sakura.txt","r",encode="utf-8")
        print(f.read())
    except FileNotFoundError:
        print("û�ҵ��ļ�~")
    except file