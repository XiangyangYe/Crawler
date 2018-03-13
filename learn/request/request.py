# import requests

# url = "https://www.baidu.com"
# response = requests.get(url)
# print(type(response))
# print(response.status_code)
# # print(type(response.text))
# # print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))

# ===================================================================
#直接reponse.txt有时候会出现乱码
# import requests

# url = "https://www.baidu.com"
# response = requests.get(url)
# response.encoding = 'utf-8'
# print(response.text)

# ===========================各种请求方式=============================
# import requests
# requests.post("http://httpbin.org/post")
# requests.put("http://httpbin.org/put")
# requests.delete("http://httpbin.org/delete")
# requests.head("http://httpbin.org/get")
# requests.options("http://httpbin.org/get")

# ------------------------------请求--------------------------------
#基本GET请求--------------------------------------------------
# import requests

# url = "http://httpbin.org/get"
# response = requests.get(url)
# print(response.text)

#带参数的GET请求-----------------------------------------------
# import requests

# url = 'http://httpbin.org/get?name=yexiangyang&age=25'
# response = requests.get(url)
# print(response.text)

# 如果我们想要在URL查询字符串传递数据，通常我们会通过httpbin.org/get?key=val
# 方式传递。Requests模块允许使用params关键字传递参数，以一个字典来传递这些参数，
# 例子如下：
# import requests
# data = {
#     "name":"yexiangyang",
#     "age":25
# }
# response = requests.get("http://httpbin.org/get",params=data)
# print(response.url)
# print(response.text)
# 上述两种的结果是相同的，通过params参数传递一个字典内容，从而直接构造url
# 注意：第二种方式通过字典的方式的时候，如果字典中的参数为None则不会添加到
# url上

# 解析Json----------------------------------------------------
# import requests
# import json

# url = "http://httpbin.org/get"
# response = requests.get(url)
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))

#获取二进制数据-------------------------------------------------
# 在上面提到了response.content，这样获取的数据是二进制数据，同样的这个方法也可以用于下载图片以及
# 视频资源
#添加headers  不添加头部不让访问

# import requests

# headers = {
# 	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
# }

# response = requests.get("http://www.zhihu.com", headers = headers)
# response.encoding = 'utf-8'
# print(response.text)

#基本POST请求---------------------------------------------

# import requests

# data = {
# 	"name":"yexiangyang",
# 	"age":25
# }

# response = requests.post("http://httpbin.org/post", data=data)
# print(response.text)

#响应-----------------------------------------------------
# import requests

# response = requests.get("http://www.baidu.com")
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response.headers)
# print(type(response.cookies),response.cookies)
# print(type(response.url),response.url)
# print(type(response.history),response.history)

#测试
# import requests

# response= requests.get("http://www.baidu.com")
# if response.status_code == requests.codes.ok:
#     print("访问成功")

 # =========================requests高级用法========================
 #文件上传--------------------------------------------------
# import requests

# files = {"files":open("git.jpeg","rb")}
# response = requests.post("http://httpbin.org/post", files=files)
# print(reponse.text)

#获取cookie
# import requests

# response = requests.get("http://www.baidu.com")
# print(response.cookies)

# for key,value in response.cookies.items():
# 	print(key + "=" + value)

#会话维持---------------------------------------------------
# cookie的一个作用就是可以用于模拟登陆，做会话维持
# import requests
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)

#证书验证---------------------------------------------------
# 现在的很多网站都是https的方式访问，所以这个时候就涉及到证书的问题
# import requests

# response = requests.get("https:/www.12306.cn")
# print(response.status_code)

# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get("https://www.12306.cn",verify=False)
# print(response.status_code)

#代理设置----------------------------------------------------
# import requests

# proxies= {
#     "http":"http://183.157.191.60",
#     # "https":"http://101.132.121.157"
# }
# response  = requests.get("https://www.baidu.com",proxies=proxies)
# response.encoding = 'utf-8'
# print(response.text)

#认证设置--------------------------------------------------
# 如果碰到需要认证的网站可以通过requests.auth模块实现
# import requests

# from requests.auth import HTTPBasicAuth

# response = requests.get("http://120.27.34.24:9001/",auth=HTTPBasicAuth("user","123"))
# print(response.status_code)

# 还有一种方式
# import requests

# response = requests.get("http://120.27.34.24:9001/",auth=("user","123"))
# print(response.status_code)

#异常处理
import requests

from requests.exceptions import ReadTimeout,ConnectionError,RequestException


try:
    response = requests.get("http://httpbin.org/get",timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")