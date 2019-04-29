#!/usr/bin/python3

import requests
import re
from requests.auth import HTTPBasicAuth
# #抓取知乎文本
# data = {
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
# url = requests.get("https://www.zhihu.com/explore", headers=data)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, url.text)
#
# with open('file/req.txt', 'w+') as file:
#     for i in range(len(titles)):
#         file.write(titles[i])
#     file.close()
#取图片
req = requests.get("https://mmbiz.qpic.cn/mmbiz_png/8XkvNnTiapOMibxG63XpLgA5NgqkrkdsKDLG1HsgmIMyYscciaINw4nOYatU7lo0f6NU8PgkXS8RlWCEAOj6MXQ0Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1")

with open('file/google.png', 'wb') as file:
    file.write(req.content)
    file.close()
# #上传图片
# files = {
#     'file': open('file/lian.png', 'rb')
# }
# req2 = requests.post('http://www.httpbin.org/post', files=files)
# print(req2.text)
# #获取cookies
# req3 = requests.get('https://www.baidu.com/')
# print(req3.cookies)
# #绑定cookies登录
# hed = {
#     'method': 'GET',
#     'Host': 'www.zhihu.com',
#     'cookie': '_zap=d4f2ec86-7a31-40fa-926c-713b4410cf4a; _xsrf=ff689e83-37ce-447e-87f3-d96a8825b641; d_c0="ADDmKBeOLw-PTqBGkUIAns-ljn7lV-sL0Do=|1553669402"; capsion_ticket="2|1:0|10:1555380610|14:capsion_ticket|44:ZTExNzFkOWE2MjA1NDMzYjg0OThhYTVhYmJjM2Y1M2M=|4c654a9569ef379dde1f15740f62921b72bf5dfa82020ae0bf6d35eb15af1b19"; z_c0="2|1:0|10:1555380668|4:z_c0|92:Mi4xZ2lWVUJBQUFBQUFBTU9Zb0Y0NHZEeWNBQUFDRUFsVk52TWJjWEFEYXpRNUNXZ0h2ZmxoYm1NTjYxck05Z0dkaDNR|4f02f3fc1f65787ec5428aa98c69bddba44a0c5cd39012731d778af8ecbf5f6d"; tst=r; q_c1=e1327e148dd14799b054f3a395e88a7c|1555381836000|1555381836000; __utmc=51854390; __utmv=51854390.100--|2=registration_date=20170309=1^3=entry_date=20170309=1; __utmz=51854390.1555393044.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/explore; tgw_l7_route=060f637cd101836814f6c53316f73463; __utma=51854390.865480905.1555381843.1555393044.1555395741.3; __utmb=51854390.0.10.1555395741',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
# req4 = requests.get('https://www.zhihu.com/', headers=hed)
# with open('file/zhihu.html', 'w+') as f:
#     f.write(req4.text)
#     f.close()
# #session保持
# session = requests.Session()
# session.get('http://www.httpbin.org/cookies/set/number/123456789')
# r = session.get('http://www.httpbin.org/cookies')
# print(r.json())

# #加代理访问
# proxy = {
#     'https': 'socks5://172.16.1.217:1024'
# }
# req5 = requests.get('https://www.youtube.com/', proxies=proxy, timeout=10)
# with open('file/youtube.html', 'wb') as f:
#     f.write(req5.content)
# #带验证账号密码访问
# req6 = requests.get('http://www.liftdatav.com', auth=HTTPBasicAuth('mwteck', 'mwteck'))
# print(req6.status_code)

#正则匹配
# content = "hello 123456 world this is a Regex Demo"
# result = re.match('^hello\s(\d+)\s(\w+)', content)
# print('result的内容：', result)
# print('result group输出：', result.group())
# print('result group(1)输出：', result.group(1))
# print('result group(2)输出：', result.group(2))
#
# result1 = re.match('^hello.*Demo$', content)
# print('result1的内容：', result1)
# print('result1 group输出：', result1.group())
# #group匹配的是上面正则匹配的组，组的区分是括号，比如(\d+),所以下面两个会匹配不到
# print('result1 group(1)输出：', result1.group(1))
# print('result1 group(2)输出：', result1.group(2))
#匹配第一个匹配到的
# content1 = 'Extra stings hello 1234567 World_This is a Regex Demo Extra string'
# result3 = re.match('hello.*?(\d+).*?Demo', content1)
# result3 = re.search('hello.*?(\d+).*?Demo', content1)
# print('re.match匹配：', result3)
# print('re.search匹配：', result3)

content2 = '2016-12-15 12:00'
content3 = '2016-12-17 12:55'
content4 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
result4 = re.sub(pattern, '', content4)
print('result2:', result2)
print('result3:', result3)
print('result4:', result4)
