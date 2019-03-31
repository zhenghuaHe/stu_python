#!/usr/bin/python
# -*- coding:utf-8 -*-

import json

# json.dumps() 对数据进行编码
# json.loads() 对数据进行解码


#json序列化和反序列化
data = {'num': 1002, 'name': 'qiaozhi'}

json_str = json.dumps(data)

print('Python原始数据：', data)
print('json对象：', json_str)

#json编码转Python数据结构

data2 = json.loads(json_str)
print("data2['num']:", data2['num'])
print("data2[''name]:", data2['name'])