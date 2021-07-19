# -*- coding: utf-8 -*-
# Created by: ERMAC
# Created data: 2020/6/27
# 去除srt字幕文件中非中文字幕
import chardet


def detect_encoding(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    encode_type = chardet.detect(data)
    return encode_type['encoding']


def is_alphabet(str):
    for i in str:
        if (u'\u4e00' <= i <= u'\u9fff') or (i == '\n'):
            return False
        elif (u"\u0041" <= i <= u"\u005a") or (u"\u0061" <= i <= u"\u007a"):
            return True
        elif i == '-':
            if (u"\u0041" <= str[2] <= u"\u005a") or (u"\u0061" <= str[2] <= u"\u007a"):
                return True
            return False


def is_chinese(str):
    for i in str:
        if u'\u4e00' <= i <= u'\u9fff':
            return True
    return False


def is_timeline(str):
    return '-->' in str


def convertsub_out(inputname):
    with open(inputname, "r", encoding=detect_encoding(inputname)) as f:
        lines = f.readlines()
    with open(inputname[:-4] + "_out.srt", "w", encoding="UTF-8") as fo:
        for line in lines:
            if line.strip().isdigit() or is_timeline(line) or line == '\n' or is_chinese(line):
                fo.write(line)
            else:
                pass
    print("完成！")


if __name__ == "__main__":
    inputname = input("输入文件名：").strip()
    try:
        convertsub_out(inputname)
    except Exception as result:
        print('出现错误：', result)
