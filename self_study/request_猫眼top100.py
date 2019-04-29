#!/usr/bin/python3

import requests
import re
import json
import time


# 获取url的头部和响应码的判断
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


# 匹配模式想要的内容
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?'
        'name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>'
        '(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?'
        '</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3],
            'time': item[4],
            'score': item[5] + item[6]
        }


# 写入文件
def write_to_file(content):
    with open('file/maoyan.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


# 一次完整的抓取
def main(offset):
    html = get_one_page('https://maoyan.com/board/4?offset=' + str(offset))
    for item in parse_one_page(html):
        write_to_file(item)


# 主函数运行，在后面添加第几页
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(3)



