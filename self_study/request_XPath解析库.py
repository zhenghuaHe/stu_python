#!/usr/bin/python3

from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import requests


# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
# response = requests.get('https://maoyan.com/board/4', headers=headers)
# txt = response.text


# html = etree.parse('./file/txt.html', etree.HTMLParser())
# result = html.xpath('//div[@class="movie-item-info"]/a/text()')
# print(type(result))
# for i in range(len(result)):
#     print(result[i])
#
# text = '<li class="li-first"><a href="link.html">first ltem</a></li>'
# html = etree.HTML(text)
# result = html.xpath('//li[@class="li-first"]/a/text()')
# print(type(result))
# print(result)

html = """
<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta content="always" name="referrer" />
<title>海军节前国产航母出海 为何悬挂“日本国旗”|中国|国产航母|信号旗_新浪军事_新浪网</title>
<meta name="keywords" content="中国,国产航母,信号旗" />
<meta name="description" content="[环球网军事报道]今年4月23日，人民海军将迎来成立70周年纪念日，届时将在青岛举行“海军成立70周年多国海军活动”。在海军成立70周年纪念日前夕，“央视军事报道”微信公号披露了首艘国产航母的最新进展，公开首艘国产航母进行海试的多个画面。其" />
<meta http-equiv="Cache-Control" content="no-transform">
<meta http-equiv="Cache-Control" content="no-siteapp">
<meta name="applicable-device" content="pc,mobile">
<meta name="MobileOptimized" content="width">
<meta name="HandheldFriendly" content="true">
<link rel="mask-icon" sizes="any" href="//www.sina.com.cn/favicon.svg" color="red">
<link rel="dns-prefetch" href="//simg.sinajs.cn">
<link rel="dns-prefetch" href="//n3.sinaimg.cn">
<ui class="list">
<li class="element">Foo</li>
</ui>
<link rel="alternate" type="application/rss+xml" href="//rss.sina.com.cn/news/marquee/ddt.xml" title="新闻中心_新浪网">
<meta name="msvalidate.01" content="0EBC6AF737F6405C0F32D73B4AA6A640" />
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/> 
<link rel="apple-touch-icon" href="//i0.sinaimg.cn/dy/news3.png">
<meta name="stencil" content="PGLS000466">
<meta name="publishid" content="hvhiqax3841848" />
<meta name="comment" content="jc:comos-hvhiqax3841848" />
<meta name="sudameta" content="comment_channel:jc;comment_id:comos-hvhiqax3841848" />
<meta name='sinaPlistaAD' content='{"article":"false","articleID":"artibody","video":"false","photos":"false","photosID":"","buttonPDPS":"PDPS000000044086","plistaPDPS":"PDPS000000060222"}'>
<meta name="mediaid" content="环球网">
<meta name="sudameta" content="sinaog:0" />
"""

xxx = {"""
<dd>
<i class="board-index board-index-1">1</i>
<a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
<img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
<img data-src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
</a>
<div class="board-item-main">
<div class="board-item-content">
<div class="movie-item-info">
<p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
<p class="star">
主演：张国荣,张丰毅,巩俐
</p>
<p class="releasetime">上映时间：1993-01-01</p>    </div>
<div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
</div>

</div>
      </div>
"""
}

# soup = BeautifulSoup(html, 'lxml')
# # print(soup.prettify())
# # print('soup.head:', soup.title.name)
# # print('soup.attrs:', soup.contents)
# # for i,child in enumerate(soup.descendants):
# #     print(i, child)
# print(soup.find_all(name='ui'))
# print('soup.select', soup.select('ui'))

doc = pq(html)
print(doc('title'))

mov = pq(requests.get('https://maoyan.com/board/4').text)
# print('mov:', mov(' .content'))
items = mov('.content')
# print('mov_type:', items.find('p'))
print(items.html())








# cqc = pq(url="https://cuiqingcai.com")
# print('cqc:', cqc('meta'))