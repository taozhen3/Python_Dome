import pytest
import common.yaml_util

@pytest.fixture(scope="function")
def conn_database():
    print("链接数据库")
    yield
    print("关闭数据库")


# @pytest.fixture(scope="session", autouse=True)
# def clear_yaml():
#     common.yaml_util.YamlUtil().clear_extract_yaml()
