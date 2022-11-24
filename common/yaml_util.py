# 文件说明：yaml文件的读取与写入

import os

import yaml


class YamlUtil:
    # 读取extract.yml文件
    def read_extract_yaml(self):
        # 打开aml文件，读取方式为a追加，编码格式utf-8，重命名为f
        with open(os.getcwd() + "/extract.yml", mode="r", encoding='utf-8') as f:
            # 读取文件流，读取方式为FullLoader，然后赋值给value
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            print('读取成功')
            return value

    # 写入extract.yaml文件
    def write_extract_yaml(self, data):
        # w 写入yaml文件，a 追加写入
        with open(os.getcwd() + "/extract.yml", mode="a", encoding='utf-8') as f:
            # 写入的数据从data传入
            yaml.dump(data=data, stream=f, allow_unicode=True)
            print('写入成功')

    # 清空yaml文件
    def clear_extract_yaml(self):
        # 打开yaml文件
        with open(os.getcwd() + "/extract.yml", mode="w", encoding='utf-8') as f:
            # 清空文件
            f.truncate()
            print('清空成功')

    # 读取测试用例的yml文件
    def read_testcase_yaml(self, yaml_name):
        # 打开yml文件，读取方式为a追加，编码格式utf-8，重命名为f
        with open(os.getcwd() + "/testcase/" + yaml_name, mode="r", encoding='utf-8') as f:
            # 读取文件流，读取方式为FullLoader，然后赋值给value
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            print('读取casedata成功')
            return value
