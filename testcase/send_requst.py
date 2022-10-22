# B站2022年最牛的python接口自动化测试框架全栈测试开发技术入门到入职教程
# day1
# p2

import requests
rep = requests.request()

# 返回字符串的数据
print(rep.text)

# 返回字节格式的数据
print(rep.content)

# 返回字典格式的数据
print(reo.json())

# 返回状态码
print(rep.status_code)

# 返回状态信息
print(rep.reason)

# 返回cookie信息
print(rep.cookies)

# 返回编码格式
print(rep.encoding)

# 返回响应信息
print(rep.headers)