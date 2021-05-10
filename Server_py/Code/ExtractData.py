# ----------------------------------------------------------------------------------------------------------------------
# 文件：提取数据
# 功能：从接收到的http包中提取出有用信息与数据，并按一定格式封装为list，并传入SaveData进行数据存储
# 输入：http包，带有状态行、head、body等
# 输出：封装的数据
# 其他：封装数据的格式data_package = ['数据类型', '"字段":内容', '"字段":内容', ..., '"字段":内容']
# ----------------------------------------------------------------------------------------------------------------------

import time

datatype = ['postconfig', 'realdata', 'recycledata', 'unknow']      #数据类型


def get_data_type(package_head):        #获取数据类型
    for i in range(4):
        thistype = datatype[i]
        if package_head.find(thistype) != -1:
            break
    return thistype


def get_data_content(package_body):     #获取字段与内容
    body = package_body
    body = body.replace('\n', '')
    body = body.replace(' ','')
    body = body.replace('{','')
    body = body.replace('}', '')
    body = body.replace('"data":','')
    data = body.split(',')
    return data


def extra_data(http_package):            #提取数据
    # head = http_package.split('{')[0]          #利用'{'进行分割，body中没有’{‘时会报错
    # body = '{' + http_package.split('{', 1)[1]

    # # 正常运行 所用分割代码
    head = http_package.split('\r\n\r\n', 1)[0]     #利用http报文中head和body的分行来分割
    body = http_package.split('\r\n\r\n', 1)[1]

    # # test HttpPackgeFile 所用分割代码
    # head = http_package.split('\n\n', 1)[0]     #利用http报文中head和body的分行来分割
    # body = http_package.split('\n\n', 1)[1]

    save_time = "time:" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    data_package = list()                        #封装数据
    data_package.append(get_data_type(head))
    data_package.append(save_time)
    content = get_data_content(body)
    for i in range(len(content)):
        data_package.append(content[i])
    return data_package


if __name__ == "__main__":
    f = open('../SourceFile/HttpPackageFile/postconfig.txt')
    http_package = f.read()
    print(extra_data(http_package))
    # f = open('SourceFile/CheckCode/checkcode.txt')