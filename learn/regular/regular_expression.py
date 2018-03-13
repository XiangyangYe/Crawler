# re.match()
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
# 语法格式：
# re.match(pattern,string,flags=0)

import re

content = "hello 123 4567 World_This is a regex Demo"
result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)
print(result.group())
print(result.span())

# 泛匹配

import re
content = "hello 123 4567 World_This is a regex Demo"
result = re.match("^hello.*Demo$",content)
print(result)
print(result.group())
print(result.span())

#匹配目标

import re
content= "hello 1234567 World_This is a regex Demo"
result = re.match('^hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

#贪婪匹配

import re

content= "hello 1234567 World_This is a regex Demo"
result= re.match('^hello.*(\d+).*Demo',content)
print(result)
print(result.group(1))

#非贪婪模式

# result= re.match('^he.*?(\d+).*Demo',content)

#匹配模式
#换行问题，re.S匹配换行内容

import re

content = """hello 123456 world_this
my name is yexiangyang
"""

result =re.match('^he.*?(\d+).*?yexiangyang$',content,re.S)
print(result)
print(result.group())
print(result.group(1))

#转义

import re

content = "price is $5.00"
result = re.match('^price.*\$5\.00',content)
print(result)
print(result.group())

#re.search
#re.serach 扫描整个字符串返回第一个成功匹配的结果

import re

content = "extra things hello 123455 world_this is a Re Extra things"
result = re.search('hello.*?(\d+).*?Re',content)
print(result)
print(result.group())
print(result.group(1))

# 注意：所以为了匹配方便，我们会更多的用search，不用match,match必须匹配头部，所以很多时候不是特别方便

import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))

# re.findall
# 搜索字符串，以列表的形式返回全部能匹配的子串
#example 1
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
	print(result)
	print(result[0], result[1], result[2])

#example 2

import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
print(results)
for result in results:
	print(result[1])

#re.sub
# 替换字符串中每一个匹配的子串后返回替换后的字符串
# re.sub(正则表达式，替换成的字符串，原字符串)

import re

content = content = "Extra things hello 123455 World_this is a regex Demo extra things"
content = re.sub('\d+', '', content)
print(content)

# 例子2,在有些情况下我们替换字符的时候，还想获取我们匹配的字符串，然后在后面添加一些内容，可以通过下面方式实现：

import re

content = "Extra things hello 123455 World_this is a regex Demo extra things"
content = re.sub('(\d+)',r'\1 7890',content)
print(content)

#re.compile
# 将正则表达式编译成正则表达式对象，方便复用该正则表达式

import re
content= """hello 12345 world_this
123 fan
"""

pattern =re.compile("hello.*fan",re.S)

result = re.match(pattern,content)
print(result)
print(result.group())