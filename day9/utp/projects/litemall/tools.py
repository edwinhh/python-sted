from utils.utils import get_value
from utils.request import MyRequest
from config.setting import log
from urllib import parse
from .const import host


class AdminLogin:
    '''admin登录'''
    url = parse.urljoin(host, '/admin/auth/login')
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_token(self):
        data = {'username': self.username, 'password': self.password}
        req = MyRequest(self.url, 'post', data=data, is_json=True)
        token = get_value(req.response, 'token')
        log.debug("登录的返回结果，%s"%req.response)
        if token:
            return token
        log.error('litemall：登录失败' % req.response)
        raise Exception('登录失败，错误信息%s' % req.response)


class WxLogin(AdminLogin):
    '''Wx登录'''
    url = parse.urljoin(host, '/wx/auth/login')
