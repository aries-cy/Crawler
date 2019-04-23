# get请求实战：实现百度信息的自动搜索

import urllib.request,re

key_wd = "python3爬虫get请求"
key_wd = urllib.request.quote(key_wd)
#page = (num-1)*10
for i in range(1,10):
    # 根据源代码写出正则表达式
    url = "http://www.baidu.com/s?wd="+key_wd+"&pn="+str((i-1)*10)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    pat = '"title":"(.*?)",'
    result = re.compile(pat).findall(data)
    for x in range(0,len(result)):
        print(result[x])