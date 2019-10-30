import hashlib
# import md5 python2
# s='1'
#
# # m = hashlib.md5( s )
# m = hashlib.sha224( s.encode() )
# result = m.hexdigest() #获取加密后的结果
# print(result)
# #撞库 #加盐
# salt='24dfw32R@#@#@$'
# password = input('password:')
# password += salt
# m = hashlib.md5( password.encode() )
# result = m.hexdigest() #获取加密后的结果
# print(result)

def md5(s,salt=''):
    new_s = str(s) + salt
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()

# import base64 #能加密，也能解密
# s='https://www.cnblogs.com/zanjiahaoge666/p/7242642.html'
# b = base64.b64encode( s.encode() ) #加密
# result= b.decode()
# print(result)
#
# b = base64.b64decode( '5ZOI5ZOI5ZOI5ZOI' ) #解密
# print(b.decode())

