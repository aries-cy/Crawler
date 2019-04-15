import re
import urllib.request

data = urllib.request.urlopen("https://gitchat.csdn.net/?utm_source=csdn_toolbar").read().decode("utf-8")
pat = "<h3 class=\"item_title_m\">(.*?)</h3>"
rst = re.compile(pat).findall(data)
print(rst)