host = 'http://api.nnzhp.cn/'

login_url = '/api/login'

goods_urls = '/api/goods'

from urllib import parse
new_url = parse.urljoin(host,login_url) #拼url
result = parse.unquote_plus('https://www.baidu.com/s?wd=%E7%99%BE%E6%B5%8B')
#url解码
s = parse.quote_plus("https://www.baidu.com/s?wd=今天中午吃什么")#url编码
print(s)