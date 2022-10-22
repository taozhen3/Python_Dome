# B站2022年最牛的python接口自动化测试框架全栈测试开发技术入门到入职教程
# day1
# p2 p3

import requests

# rep = requests.request()
#
# # 返回字符串的数据
# print(rep.text)
#
# # 返回字节格式的数据
# print(rep.content)
#
# # 返回字典格式的数据
# print(reo.json())
#
# # 返回状态码
# print(rep.status_code)
#
# # 返回状态信息
# print(rep.reason)
#
# # 返回cookie信息
# print(rep.cookies)
#
# # 返回编码格式
# print(rep.encoding)
#
# # 返回响应信息
# print(rep.headers)

# 发送git请求 ctrl+鼠标左键查看源代码
url = "https://api.weixin.qq.com/cgi-bin/token"
data = {
    "grant_type": "client_credentials",
    "appid": "wx6b11b3efd1cdc290",
    "secret": "106a9c6157c4db5f6029918738f9529d",
}
rep = requests.get(url, params=data)
print(rep.json())

# 发送post请求
requests.post(url, data=data)