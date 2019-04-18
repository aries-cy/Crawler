import re
import urllib.request
import mysql.connector

data = urllib.request.urlopen("https://gitchat.csdn.net/?utm_source=csdn_toolbar").read().decode("utf-8")
result = re.findall(r'<h3 class="item_title">(.*?)</h3>.*?<p class="item_name">(.*?)</p>',data,re.S|re.M)
books = []
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="cy"
)
cursor = db.cursor()
sql = "insert into book (title,author) values (%s,%s)"
for title,name in result:
    val = (title,name)
    books.append(val)
cursor.executemany(sql,books)
db.commit()
sql = "select * from  book"
cursor.execute(sql)
rst = cursor.fetchall()
for x in rst:
    print(x)
