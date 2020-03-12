# -*- coding: utf-8 -*-
# Created by: ermac-cw
# Created data: 2020/6/9
# 很简单的一个爬取京东关键字相关的所有品牌名
import requests
import re

keyword = "健身器材"


def brands_extract(keyword):
    url = (
        "https://so.m.jd.com/ware/search.action?keyword="
        + str(keyword)
        + "&searchFrom=home&sf=11&as=1"
    )
    head = {
        "user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }
    r = requests.get(url, headers=head)
    r.encoding = "utf-8"
    content = r.text
    reg = re.findall(r'"value":"(.*?)\|=\|",', content)  # 正则解析
    print(reg[0].replace("|=|", ","))  # 清洗格式


if __name__ == "__main__":
    brands_extract(keyword)
