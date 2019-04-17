import re
import urllib.request

from example.Book import Book

data = urllib.request.urlopen("https://gitchat.csdn.net/?utm_source=csdn_toolbar").read().decode("utf-8")
#patTitle = "<h3 class=\"item_title_m\">(.*?)</h3>"
result = re.findall(r'<h3 class="item_title">(.*?)</h3>.*?<p class="item_name">(.*?)</p>',data,re.S|re.M)
print(result)
#rst = re.compile(patTitle).findall(data)
books = []
for title,name in result:
    book = Book(title,name)
    books.append(book)

for msg in books:
    print(Book.display_author(msg))