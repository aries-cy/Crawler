import urllib.request
import urllib.parse

url = "https://www.douban.com/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request).read().decode()

print(response)
