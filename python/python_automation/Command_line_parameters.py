sys.argv 获取命令行参数

python sys 标准库里面有三个文件描述符 分别是stdin stdout stderr  分别代表标准输入 标准输出 错误输出

使用getpass 库 获取密码  不会再命令行 看到 密码
import getpass
user      = getpass.getuser()
passwd = getpass.getpass('your password: ')
print(user,passwd) 


使用ConfigParse解析配置文件
git工作的时候 会去读取 ~/.gitconfig 
mysql工作的时候  /etc/mysql/my.cnf
pip工作的时候会读取 ~/.pip/pip.conf
