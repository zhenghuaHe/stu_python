import requests



url = "http://wechat.v3.api.2012iot.com/api-python-wechat/alarm/wxAlarm"
values = {
        "evId": "101945507171782372",
        "trap": "1",
        "description": "222222222"
}

result = requests.post(url,data=values)
print(result)
print(result.status_code,result.text)


