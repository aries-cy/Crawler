import urllib.request

url = 'http://www.oschina.net/'

#添加头部，伪装浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
#Request类的实例，构造时需要传入Url,Data，headers等等的内容
resquest = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(resquest).read()
html = response.decode('utf-8')
print(html)

