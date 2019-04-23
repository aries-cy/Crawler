# Crawler
## python爬虫  
 * ###  1.正则表达式  
 + ####   a.元字符：  
   -  .  匹配任意字符（不包括换行符）  
   -  ^  匹配开始位置，多行模式下匹配每一行的开始  
   -  $  匹配结束位置，多行模式下匹配每一行的结束  
   -  \*  匹配前一个元字符0到多次  
   -  \+  匹配前一个元字符1到多次  
   -  ?  匹配前一个元字符0到1次  
   -  {m,n}  匹配前一个元字符m到n次  
   -  \d 匹配一个数字，相当与[0-9]  
   -  \D 匹配一个非数字  
   -  \s 匹配任意空白字符  
   -  \S 匹配任意非空白字符  
   -  \w 匹配数字、字母、下划线中任意一个字符  
   -  \W 匹配非数字、字母、下划线  
 + ####   b.模式：
    - I 忽略大小写的匹配模式
    ```python
       s = 'hello World!'
       regex = re.compile("hello world!", re.I)
    ```
    - S '.'可以匹配任何字符，包括换行符
    - X 冗余模式，忽略正则表达式中的空白和#号的注释
 + ### c.函数：
    - re.compile【全局匹配】
    ```python
       s = '''first line
           second line
           third line'''
       regex = re.compile(".+")
       print(regex.findall(s))
       # output> ['first line', 'second line', 'third line']
    ```
    - re.search【扫描整个字符串并返回第一个成功的匹配】
    - re.match 【从第一个字符开始匹配】
    - sub(pattern, repl, string, count=0, flags=0) 【替换函数】
    ```python
       #将正则表达式pattern匹配到的字符串替换为rep1制定的字符串，count用于指定最大替换次数
       s = "the sum of 7 and 9 is [7+9]."
       print(re.sub('\[7+9\]','16',s))
       # output> the sum of 7 and 9 is 16.
    ```
 * ###  2.urllib模块
    + ### 该库有4个模块，分别是：
        + urllib.request
        + urllib.error
        + urllib.parse
        + urllib.robotparser