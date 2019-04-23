import urllib.request
import urllib.robotparser

# urlretrieve:将url定位到的html文件下载到本地
urllib.request.urlretrieve("http://www.baidu.com","D:\\test\\bai_du.html")

# urlcleanup()的应用，可以将urlretrieve()中的缓存清理掉
urllib.request.urlcleanup()

#info()  查看相应的简介
file = urllib.request.urlopen("http://www.baidu.com")
print(file.info())

# getcode()  为了输出状态码
code = file.getcode()
print(code)

# geturl()  获取当前页面的url
url = file.geturl()
print(url)
