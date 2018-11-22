import requests
import os
a = 1
while True:
    headers = {
    'agent': 'Mozilla/5.0 (Windows NT 20; Win20; x20; rv:62.0) Gecko/20100101 Firefox/62.0'
    }
    response1 = requests.get('http://api.t5.2012iot.com/api-elevator-python/check',headers = headers)
    # print(response1.status_code)
    os.popen("sleep 1")
    a += 1
    print(a)
