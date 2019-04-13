import re

#原子

#元字符
'''
. 除换行任意字符
^ 匹配开始位置
$ 匹配结束位置
* 0\1\多次
? 0\1次
+ 1\多次
{n} 恰好多次
{n,} 至少n次
{n,m} 至少n次，至多m次
| 模式选择符 或
'''

string = "cao_yang@163.com"
pat = "^c.*$"
print(re.search(pat,string))

'''
模式修正符

I 匹配的时候忽略大小写*
M 多行匹配*
L 本地化识别匹配
U Unicode
S 让.匹配包括换行*
'''

String = "Python"
pat = "pyt"
print(re.search(pat,String,re.I))


'''
贪婪模式：尽可能多的去匹配(默认贪婪模式)
懒惰模式：尽可能少的去匹配(.*?)
'''
string = "python_yn"
pat = "p.*n"
pat2 = "p.*?n"
print(re.search(pat,string))
print(re.search(pat2,string))

'''
正则表达式函数
match : 从头匹配
search :任意位置匹配
全局匹配函数:格式：re.compile(正则表示式).findall(数据)
'''
string = "cao_yang_coo_yg_yug"
pat = "y.*?g"
rst = re.compile(pat).findall(string)
print(rst)
