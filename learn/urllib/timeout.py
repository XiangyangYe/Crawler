import urllib.request

reponse = urllib.request.urlopen('http://www.baidu.com', timeout = 1)
print(reponse.read().decode('utf-8'))
print(reponse.read)


#=====================================================================#
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

#响应类型、状态码、报头
import urllib.request

reponse = urllib.request.urlopen('https://www.baidu.com')
print(type(reponse))
# ----------------------------------------------------------------
# request 
# 设置Headers
import urllib.request

request = urllib.request.Request('https://python.org')
reponse = urllib.request.urlopen(request)
print(reponse.read().decode('utf-8'))
#---------------------------------------------------------------
#需要头部信息才能访问
from urllib import request,parse

url = 'http://www.baidu.com'
headers = {
	'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	'Host':'baidu.com'
}
dict = {
	'name': 'yexiangyang'
}

data = bytes(parse.urlencode(dict),encoding = 'utf-8')
req = request.Request(url = url, data = data, headers = headers, method = 'POST')
reponse = request.urlopen(req)
print(reponse.read().decode('utf-8'))

#添加请求头的第二种方式
from urllib import request,parse

url = 'http://baidu.com'
dict = {
	'name': 'Vanallen'
}

data = bytes(parse.urlencode(dict), encoding = 'utf-8')
req = request.Request(url = url , data = data, method = 'POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
reponse = request.urlopen(req)
print(reponse.read().decode('utf-8'))

# ===========================================================================
#高级用法各种handler
#代理，ProxyHandler

import urllib.request

url = 'http://www.baidu.com'
proxy_handler = urllib.request.ProxyHandler(
		{
		'http':'http://101.132.121.157'
		# 'https':'https://101.132.121.157'
		}
	)

opener = urllib.request.build_opener(proxy_handler)
reponse = opener.open(url)
print(reponse.read())
# ------------------------------------------------------------------------------
#cookie，HTTPCookiProceseor
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
reponse = opener.open('http://baidu.com')
for item in cookie:
	print(item.name + "=" + item.value)

#cookie http.cookiejar.LWPCookieJar()
import http.cookiejar,urllib.request

filename  = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard = True, ignore_expires = True)

# #同样的如果想要通过获取文件中的cookie获取的话可以通过load方式，当然用哪种方式写入的，就用哪种方式读取。
import http.cookiejar, urllib.request
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_discard = True, ignore_expires = True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
reponse = opener.open('http://www.baidu.com')
print(reponse.read().decode('utf-8'))

#=======================================================================#
#异常处理
from urllib import request,error

try:
	reponse = request.urlopen("http://pythonsite.com/111.html")
except error.URLError as e:
	print(e.reason)


#HTTPError:code reason headers
from urllib import request, error

try:
	response = request.urlopen("http://pythonsite.com/111.html")
except error.HTTPError as e:
	print(e.reason)
	print(e.code)
	print(e.headers)
except error.URLError as e:
	print(e.reason)
else:
	print("request successfully")

#同时，e.reason也可以做更深入的判断
import socket
from urllib import request, error

try:
	reponse = request.urlopen("http://pythonsite.com/111.html")
except error.URLError as e:
	print(type(e.reason))
	if isinstance(e.reason, socket.timeout):
		print("time out")

#------------------------------------------------------------------------
#URL解析
from urllib.parse import urlparse

result = urlparse('"http://www.baidu.com/index.html;user?id=5#comment"')
print(result)

#urlunpars 拼接
from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123', 'commit']
print(urlunparse(data))

#这个方法可以将字典换为url参数
from urllib.parse import urlencode

params = {
	"name": "yexiangyang",
	"age": 23,
}

base_url = "http://baidu.com?"

url = base_url + urlencode(params)
print(url)
