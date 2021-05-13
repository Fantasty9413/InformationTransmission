import socket
import time
import json
import logging
import Log
from Code import ExtractData
from Code import SaveData


def get_response_body(type):
    time_unix = int(time.time())
    if type == ExtractData.datatype[0]:
        f = open('../SourceFile/CheckCode/checkcode.txt', encoding='utf-8')
        check_code = f.read()  # 读取校对码
        message = [{"code": 200, "data":"configok", "from": check_code}]
    elif type == ExtractData.datatype[1]:
        f = open('../SourceFile/CheckCode/checkcode.txt', encoding='utf-8')
        check_code = f.read()  # 读取校对码
        message = [{"code": 200, "from": check_code, "message": "success", "unix": time_unix}]
    elif type == ExtractData.datatype[2]:
        message = [{"code": 200, "message": "success"}]
    else:
        message = [{"code": 200, "message": "success"}]

    return message


def get_response(http_package):             #生成http响应内容
    response_line = 'HTTP/1.1 200 OK\r\n'

    response_head = 'Server:scu localhost\r\n'
    response_head += 'Content-Type:text/html\r\n'
    time_response = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))      #获取系统时间并将其转换为str格式
    response_head += 'time:' + time_response + '\r\n'

    # time_unix = int(time.time())
    # f = open('SourceFile/CheckCode/checkcode.txt', encoding='utf-8')
    # check_code = f.read()       #读取校对码
    # message = [{"code":200,"from":check_code,"message":"success","unix":time_unix}]

    data_package = ExtractData.extra_data(http_package)             #利用data_type来判断回复的信息内容
    message = get_response_body(data_package[0])

    # response_body = str(message)          #直接转str
    response_body = json.dumps(message)     #json转str
    # response_body = 'ok'

    response = response_line + response_head + '\r\n' + response_body
    return response


def save_httppackage(file, http_package):                   #用于存储httppackage到sourcefile以便测试
    fh = open('../SourceFile/HttpPackageFile/' + file, 'w', encoding='utf-8')
    fh.write(http_package)
    fh.close()


def save_to_excel(http_package):                            #将数据信息存储至excel文件
    data_package = ExtractData.extra_data(http_package)
    SaveData.save_data(data_package)


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 80))
    s.listen(5)

    print("waiting for connection\r\n")

    while True:
        connection, address = s.accept()
        print('接收到来自 {}:{} 的请求\r\n'.format(address[0], address[1]))
        try:
            connection.settimeout(5)
            buf = connection.recv(1024).decode('utf-8')
            # print(buf)
            # save_httppackage('recycledata.txt', buf)
            save_to_excel(buf)
            connection.send(get_response(buf).encode())
        except s.timeout:
            logging.warning('time out')
            print('time out')
        connection.close()
    return None


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost",80))
    s.listen(5)

    print("waiting for connection\r\n")

    while True:
        connection,address = s.accept()
        print('接收到来自 {}:{} 的请求\r\n'.format(address[0], address[1]))
        try:
            connection.settimeout(5)
            buf = connection.recv(1024).decode('utf-8')
            # print(buf)
            # save_httppackage('recycledata.txt', buf)
            save_to_excel(buf)
            connection.send(get_response(buf).encode())
        except s.timeout:
            print('time out')
        connection.close()
    # print(time.time())
    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    # print(get_response())