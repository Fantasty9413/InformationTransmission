import logging

#   初始化日志对象
logging.basicConfig(
#   日志级别
level = logging.DEBUG,
# 日志格式
# 时间、代码所在文件名、代码行号、日志级别名字、日志信息
format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
 # 打印日志的时间
datefmt = '%a, %d %b %Y %H:%M:%S',
# 日志文件存放的目录（目录必须存在）及日志文件名
filename = '../Log/report.log',
 # 打开日志文件的方式
filemode = 'a'      #a = add 追加, w = write 新建文件
)

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')