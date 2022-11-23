# B站讲的最详细的Python接口自动化测试实战教程全集（实战最新版）
# day1
# p2 p3 p4 p5 p6 p7
import json
import pytest
import requests
import json
from common import yaml_util

class Test_login:
    def setup(self):
        print("每条用例执行前执行")

    def teardown(self):
        print("每条用例执行后执行")

    def test_login1(self):
        url = "https://boss.sdf.testxyy.cn/backApi/sxx/uas/UserBasicMS/bossInteraction/doLogin"
        headers = {"utype": "boss", "Content-Type": "application/json", "EncryptType": "AES"}
        data = {
            "userName": "amSRwwDvBGjfu638KBwAbA==",
            "password": "VO4AUibpUy2SUAdzYFm40Q=="
        }
        rep = requests.post(url=url, data=json.dumps(data), headers=headers)
        token = rep.json()['data']['authorization']
        yaml_util.YamlUtil().write_extract_yaml({"token": token})
        # YamlUtil().write_extract_yaml({"token": token})

    def test_login2(self, conn_database):
        url = "https://boss.sdf.testxyy.cn/backApi/sxx/uas/UserBasicMS/bossInteraction/doLogin"
        headers = {"utype": "boss", "Content-Type": "application/json", "EncryptType": "AES"}
        data = {
            "userName": "amSRwwDvBGjfu638KBwAbA==",
            "password": "VO4AUibpUy2SUAdzYFm40Q=="
        }
        rep = requests.post(url=url, data=json.dumps(data), headers=headers)
        token = rep.json()['data']['authorization']
        value = yaml_util.YamlUtil().read_extract_yaml()
        print(value)
