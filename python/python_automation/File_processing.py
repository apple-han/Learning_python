BASE_DIR = os.path.dirname(os.path.dirname(os.path.adspath(__file__)))  根目录
a = 'nihao'
a = '\'nihao'

a = '''  这个可以解决转义的问题'''

字符串的两大特性：
字符串是不可变的
字符串是字符的有序集合
字符串的函数
len(s)
s[0]
'x' in s
str.split()
str.upper()

与大小相关的函数
upper 转化为大写
lower 转化为小写
isupper 判断字符串是否是大写
islower 判断字符串是否是大写
swapcase 将字符串大写转化为小写 小写转化为大写
capitalize  将首字母转化为大写
istitle      判断字符串是不是一个标题

s.isalpha: 如果字符串只包含字母，并且非空，则返回True，否则返回False

s.isalnum: 如果字符串只包含字母和数字，并且非空，则返回True，否则返回False

s.isspace: 如果字符串只包含空格，制表符，换行符，并且非空，则返回True，否则返回False

s.isdecimal: 如果字符串只包含数字，并且非空，则返回True，否则返回False

s = "lai ming xing"
s.startwith('lai') // true
s.endwith('lai') // false

",".join(['a','b','c'])  //可传入任何可迭代对象
 

