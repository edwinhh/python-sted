import itsdangerous
from django.conf import settings
from .const import token_expire
class Token:
    tjss = itsdangerous.TimedJSONWebSignatureSerializer(settings.SECRET_KEY, expires_in=token_expire)

    @classmethod
    def create_token(cls,data):
        token =  cls.tjss.dumps(data).decode()
        return token

    @classmethod
    def check_token(cls,token):
        try:
            data = cls.tjss.loads(token)
        except:
            return False
        return data

