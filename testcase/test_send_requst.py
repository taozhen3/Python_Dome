# B站讲的最详细的Python接口自动化测试实战教程全集（实战最新版）
# p2 p3 p4 p5 p6 p7

import json
import pytest
import requests
import json
from common.yaml_util import YamlUtil


class Test_login:
    def setup(self):
        print("每条用例执行前执行")

    def teardown(self):
        print("每条用例执行后执行")

    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_token.yml'))
    def test_login1(self, caseinfo):
        url = caseinfo['request']['url']
        headers = caseinfo['request']['headers']
        data = caseinfo['request']['data']
        rep = requests.post(url=url, data=json.dumps(data), headers=headers)
        token = rep.json()['data']['authorization']
        # 断言

        if rep.status_code == 200:
            YamlUtil().write_extract_yaml({"token": token})
        else:
            print('用例异常')


    #
    # def test_login2(self, conn_database):
    #     url = "https://boss.sdf.testxyy.cn/backApi/sxx/uas/UserBasicMS/bossInteraction/doLogin"
    #     headers = {"utype": "boss", "Content-Type": "application/json", "EncryptType": "AES"}
    #     data = {
    #         "userName": "amSRwwDvBGjfu638KBwAbA==",
    #         "password": "VO4AUibpUy2SUAdzYFm40Q=="
    #     }
    #     rep = requests.post(url=url, data=json.dumps(data), headers=headers)
    #     token = rep.json()['data']['authorization']
    #     print(token)
    #     common.yaml_util.YamlUtil().write_extract_yaml({"token": token})
