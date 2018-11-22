import requests


# def test_url():
        # pass

url = "http://api.t4.2012iot.com/api-python-wechat/alarm/alarm_list"
requests_url  = requests.get(url)

headers = {
        "Authorization": "MTc2OF90b2tlbl8xNTM5ODQ3MDE0Mzc3LCwsMTUzOTg0NzAxNDM3Nw=="
}

result = requests.get(url,headers=headers)
print(result)
print(result.status_code,result.text)


