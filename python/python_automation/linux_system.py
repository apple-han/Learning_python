import tarfile

压缩包的库
with tarfile.open('tarfile_add.tar') as f:
for member_info in t.getmembers():
print(member_info.name)



1,两个目录中的文件到底有多少差别？
2，系统中有多少重复文件？
3，如何找到并删除系统中重复的文件

import filecmp

filecmp.cmp('a.txt', 'b.txt')


os模块是对操作系统的接口进行封装，主要作用是跨平台的。shutil 模块包含复制，移动，重命名，和删除文件以及目录的函数，主要的作用是管理文件和目录
import 
shutil.copy('a.py', 'b.py')

shutil.move('b.py', 'dir1')
shutil.rmtree('dir1')



判断文件的操作权限

def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + ' does not exists')
    elif not os.access(filename, os.R_OK):
        os.chmod(filename, 0777)
    else:
        with open(filename) as f:
            print(f.read())

if __name__ == '__main__':
    main()

linux命令
ctrl +r 搜索之前使用过的命令  并把历史记录保存在 ~/.bash_history

下面是我使用过的最多的10个命令
import os
from collections import Counter

c = Counter()

with open(os.path.expanduser('~/.bash_history')) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]]+=1

print c.most_common(10)
try:
f = open('data.txt')
print f.read()
finally:
f.close()

下面的方式比较pythonic
with open('data.txt') as f:
print f.read()

python提供了三个读相关的函数 分别是read readline readlines 

read: 读取所有的数据
readline：一次读取一行
readlines 讲文件内容存到一个列表当中 列表的每一行 对应文件的一行

两个写函数：
write 把字符串写到文件中，并返回写入的字符数
writelines 写一个字符串列表到文件中

还可以使用 print 把结果输出到文件中
from __future__ import print_function

with open('data.txt') as inf, open('out.txt', 'w') as outf:
    for line in inf:
        print(*[word.capitalize() for word in line.split()], file=outf)

python的for循环不止可以遍历 可迭代序列 还可以迭代可迭代对象
