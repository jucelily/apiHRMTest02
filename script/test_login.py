import unittest
from api.login_api import LoginApi
from utils import assert_common
import logging


class TestIHRMLogin(unittest.TestCase):
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

    def test01_login_success(self):
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        logging.info(jsonData)
        # 调试输出登陆接口返回的数据，日志输出只能用{}作为占位
        logging.info("登录成功接口返回的数据为{}".format(jsonData))
        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应码状态
        # self.assertEqual(True,jsonData.get("success"))#断言success
        # self.assertEqual(10000,jsonData.get("code"))#断言code
        # self.assertEqual("操作成功！",jsonData.get("message"))#断言message
        assert_common(self,response,200,True,10000,"操作成功")
    def test02_username_is_not_exist(self):
        #调用封装的接口
        response=self.login_api.login('13900000002','123456')
        #接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info('账号不存在时输入的数据为：{}'.format(jsonData))
        assert_common(self,response,200,False,20001,"用户名或密码错误")
    def test03_password_is_error(self):
        #调用封装的接口
        response=self.login_api.login('13800000002','error')
        #接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info('密码错误时输出的数据为：{}'.format(jsonData))
        assert_common(self,response,200,False,20001,"用户名或密码错误")
    def test04_username_have_special_char(self):
        #调用封装的接口
        response=self.login_api.login('13*&0000002','error')
        #接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info('用户名有特殊符号时输出的数据为：{}'.format(jsonData))
        assert_common(self,response,200,False,20001,"用户名或密码错误")
    def test05_username_is_empty(self):
        #调用封装的接口
        response=self.login_api.login('','error')
        #接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info('账号为空时输入的数据为：{}'.format(jsonData))
        assert_common(self,response,200,False,20001,"用户名或密码错误")
    def test06_password_is_empty(self):
        #调用封装的接口
        response=self.login_api.login('13800000002','')
        #接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info('密码为空时输出的数据为：{}'.format(jsonData))
        assert_common(self,response,200,False,20001,"用户名或密码错误")
    def test07_username_have_chinese(self):
        #调用封装的接口
        response=self.login_api.login('13就00000002','123456')
        #接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info('账号中有中文时输出的数据为：{}'.format(jsonData))
        assert_common(self,response,200,False,20001,"用户名或密码错误")
    def test08_username_middler_have_space(self):
        #调用封装的接口
        response=self.login_api.login('13 00000002','123456')
        #接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info('账号中间有空格时的输出数据为：{}'.format(jsonData))
        assert_common(self,response,200,False,20001,"用户名或密码错误")