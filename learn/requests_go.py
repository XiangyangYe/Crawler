import requests

# r = requests.get('https://github.com/timeline.json')
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/head')
# r = requests.options('http://httpbin.org/options')

# ==============================================================================#
# payload = {'key1' : 'value1', 'key2' : 'value2'}
# r = requests.get('http://httpbin.org/get', params = payload)
# print(r.url)
#-------------------------------------------------------------------------------#
# payload = {'key1' : 'value1', 'key2' : ['value2', 'value3']}
# r = requests.get('http://httpbin.org/get', params = payload)
# print(r.url)
#===============================================================================#

# r = requests.get('http://github.com/timeline.json')
# print(r.text)
# print(r.encoding)
# print(r.content)

#===============================================================================#
#json

# r = requests.get('http://github.com/timeline.json')
# print(r.json())

#===============================================================================#
#