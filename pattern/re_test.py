import re

'''
匹配.com和.cn网址
'''

string = "<a href='ftp://www.baidu.com'>百度首页</a>'"
pat = "[a-zA-Z]+://[^\s]*[.com|.cn]"
rst = re.compile(pat).findall(string)
print(rst)

'''
匹配电话号码
'''
string = "cao-yang-liu-021-89332432432-x-yu-0733-823764872334_ha"
pat = "\d{4}-\d{7}|\d{3}-\d{8}"
rst = re.compile(pat).findall(string)
print(rst)
