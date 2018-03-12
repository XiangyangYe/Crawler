# import urllib.request

# reponse = urllib.request.urlopen('http://www.baidu.com', timeout = 1)
# # print(reponse.read().decode('utf-8'))
# print(reponse.read)


#=====================================================================#
# import socket
# import urllib.request
# import urllib.error

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

#响应类型、状态码、报头
# import urllib.request

# reponse = urllib.request.urlopen('https://www.baidu.com')
# print(type(reponse))
# ----------------------------------------------------------------
#request 
#设置Headers
# import urllib.request

# request = urllib.request.Request('https://python.org')
# reponse = urllib.request.urlopen(request)
# print(reponse.read().decode('utf-8'))
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