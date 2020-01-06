import unittest
from api.login_api import LoginApi
from utils import assert_common, read_login_data
import logging
from parameterized.parameterized import parameterized


class TestIHRMLoginPara(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登陆类
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
    @parameterized.expand(read_login_data)
    def test01_login_success(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile, password)
        # 接收返回的json数据
        jsonData = response.json()
        logging.info(jsonData)
        # 调试输出登陆接口返回的数据，日志输出只能用{}作为占位
        logging.info("登录接口返回的数据为{}".format(jsonData))
        assert_common(self, response, http_code, success, code, message)
