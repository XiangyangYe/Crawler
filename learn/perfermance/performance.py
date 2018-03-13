# 简单的循环串行
# import requests

# url_list = [
# 	'http://www.baidu.com',
# 	'http://www.feixiaohao.com',
# 	'http://www.cnblogs.com/'
# ]

# for url in url_list:
# 	reponse = requests.get(url)
# 	print(reponse.text)
# =======================================================================
#通过线程池

# import requests
# from concurrent.futures import ThreadPoolExecutor

# def fetch_request(url):
# 	result = requests.get(url)
# 	print(result.text)

# url_list = [
# 	'http://www.baidu.com',
# 	'http://www.feixiaohao.com',
# 	'http://www.cnblogs.com/'
# ]

# pool = ThreadPoolExecutor(10)

# for url in url_list:
# 	#去线程池中获取一个线程，去执行fetch_request方法
# 	pool.submit(fetch_request, url)

# pool.shutdown(True)

#线程池+回调函数

# from concurrent.futures import ThreadPoolExecutor
# import requests

# def fetch_async(url):
# 	response = requests.get(url)
# 	return response

# def callback(future):
# 	print(future.result().text)

# url_list = [
# 	'http://www.baidu.com',
# 	'http://www.feixiaohao.com',
# 	'http://www.cnblogs.com/'
# ]


# pool = ThreadPoolExecutor(5)

# for url in url_list:
#     v = pool.submit(fetch_async,url)
#     #这里调用回调函数
#     v.add_done_callback(callback)

# pool.shutdown()

# =================================================================
#通过进程池
# 通过进程池的方式访问，同样的也是取决于耗时最长的，但是相对于线程来说，进程需要耗费更多的资源，同时这里是访问url时IO操作，所以这里线程池比进程池更好
# import requests
# from concurrent.futures import ProcessPoolExecutor

# def fetch_request(url):
#     result = requests.get(url)
#     print(result.text)

# url_list = [
#     'http://www.baidu.com',
#     'http://www.bing.com',
#     'http://www.cnblogs.com/'
# ]
# pool = ProcessPoolExecutor(10)

# if __name__ == '__main__':
# 	for url in url_list:
#     #去进程池中获取一个线程，子进程程去执行fetch_request方法
#    		pool.submit(fetch_request,url)

# pool.shutdown(True)

#进程池+回调函数
from concurrent.futures import ProcessPoolExecutor
import requests


def fetch_async(url):
    response = requests.get(url)
    return response


def callback(future):
    print(future.result().text)


url_list = [
    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.cnblogs.com/'
]

pool = ProcessPoolExecutor(5)

if __name__ == '__main__':
	for url in url_list:
		v = pool.submit(fetch_async, url)
		v.add_done_callback(callback)

pool.shutdown()
