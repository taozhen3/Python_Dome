import pytest


class TestApi:

    # @pytest.mark.parametrize('args', ['张三', '李四', '王五'])
    # def test_api1(self, args):
    #     print(args)

    @pytest.mark.parametrize('name, age', [['张三', 18], ['李四', 20],  ['王五', 30]])
    def test_api2(self, name, age):
        print(name, age)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_api.py'])
