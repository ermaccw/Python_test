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


def is_alphabet(ch):
    if (u"\u0041" <= ch <= u"\u005a") or (u"\u0061" <= ch <= u"\u007a"):
        return True
    else:
        return False


def is_chinese(ch):
    for i in ch:
        if u'\u4e00' <= i <= u'\u9fff':
            return True
    return False


def is_timeline(ch):
    if ch.find('-->') >= 0:
        return True
    else:
        return False


def covertsub_out(inputname):
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
    inputname = input("输入文件名：")
    try:
        covertsub_out(inputname)
    except Exception as result:
        print('出现错误！可能原因：请去掉文件名中的空格\n', result)
