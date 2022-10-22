# B站讲的最详细的Python接口自动化测试实战教程全集（实战最新版）
# day1
# p2 p3
import json
import pytest
import requests
import json

class Test_login:
    def test_login(self):
        url = "https://boss.sdf.testxyy.cn/backApi/sxx/uas/UserBasicMS/bossInteraction/doLogin"
        headers = {"utype":"boss","Content-Type": "application/json","EncryptType": "AES"}
        data = {
            "userName": "amSRwwDvBGjfu638KBwAbA==",
            "password": "VO4AUibpUy2SUAdzYFm40Q=="
        }
        rep = requests.post(url = url, data = json.dumps(data),headers = headers)
        token = rep.json()['data']['authorization']
        print(token)

