import requests
import app
class LoginApi:
    def __init__(self):
        self.login_url=app.HOST+"/api/sys/login"
        self.headers=app.HEADERS
    #从外部接收mobile和password
    def login(self,mobile,password):
        #要发送的数据
        data={"mobile":mobile,"password":password}
        #发送登陆请求
        response=requests.post(self.login_url,json=data,headers=self.headers)
        #返回响应数据
        return response




