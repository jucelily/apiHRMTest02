import unittest
from api.login_api import LoginApi
from utils import assert_common
import logging
import app


class Login(unittest.TestCase):
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

    def test_login(self):
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        logging.info(jsonData)
        # 调试输出登陆接口返回的数据，日志输出只能用{}作为占位
        logging.info("登录成功接口返回的数据为{}".format(jsonData))
        assert_common(self, response, 200, True, 10000, "操作成功")
        # 获取令牌，并拼接成Bearer开头的字符串
        token = jsonData.get("data")
        app.HEADERS['Authorization'] = "Bearer " + token
        logging.info('保存的令牌是：{}'.format(app.HEADERS))