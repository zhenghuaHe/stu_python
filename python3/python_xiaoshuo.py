# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

base_url = "https://read.qidian.com/chapter/MkPe8hZcx6UvLUkaWbCIdw2/fWEV24MWnbBp4rPq4Fd4KQ2"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}

# if __name__ == "__main__":
#     req = requests.get(base_url,headers = headers)
#     html = req.text
#     bf = BeautifulSoup(html)
#     texts = bf.find_all('div', class_ = 'main-text-wrap')
#     print(texts[0].text.)
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/5403177.html'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html)
     texts = bf.find_all('div', id = "content", class_ = 'showtxt')
     # print(texts[0].text.replace('\xa0'*8,'\n\n'))
     print(texts)



















