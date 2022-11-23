import os
import yaml


class YamlUtil:
    # 读取extract.yml文件
    def read_extract_yaml(self):
        with open(os.getcwd() + "/extreact.yml", mode="r", encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

    # 写入extract.yaml文件
    def write_extract_yaml(self):
        with open(os.getcwd() + "/extreact.y", mode="w", encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
