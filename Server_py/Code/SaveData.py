# ----------------------------------------------------------------------------------------------------------------------
# 文件：存储数据
# 功能：将SaveData传输的数据包解码，并按照数据类型，分门别类地存到excel文件中
# 输入：SaveData传输的数据包
# 输出：存储数据的excel文件
# 其他：
#       1.封装数据的格式data_package = ['数据类型', '"字段":内容', '"字段":内容', ..., '"字段":内容']
#       2.数据类型datatype = ['postconfig', 'realdata', 'recycledata', 'unknow']，不同类型的数据存在不同的sheet
#       3.所有存储数据均放在excel表中，文件按照日期命名，命名规则 = ‘datafile’+日期，并存放在DataFile文件中
# ----------------------------------------------------------------------------------------------------------------------

import xlrd
import datetime
import logging
import Log
from xlutils.copy import copy
from shutil import copyfile
from sys import exit
from Code.ExtractData import extra_data


datatype = ('postconfig', 'realdata', 'recycledata', 'unknow')      #数据类型
writerow_sheets = [1, 1, 1, 1]        #


def get_filename():
    time_now = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = 'datafile_' + time_now + '.xls'
    return filename


def save_data(data_package):
    this_type = data_package[0]     #the type of the packed data
    num_sheet = datatype.index(this_type)       #the num of sheet to write
    writerow = writerow_sheets[num_sheet]       #the writing row of this sheet
    writerow_sheets[num_sheet] += 1

    data_split = data_package.copy()        #copy list  python的传址传值调用特性  可变对象传址调用 不可变对象传址调用
    # data_split.remove(this_type)              #去头，只留字段与内容
    try:
        data_split.remove('')                   #去掉空数据      data_split:分割后的数据
    except ValueError as e:
        data_split.remove(this_type)            #去头，只留字段与内容
    else:
        data_split.remove(this_type)

    filename = get_filename()
    try:                                                                #检测是否存在待写文件
        file = xlrd.open_workbook('../DataFiles/' + filename)
    except IOError:
        try:
            copyfile('../SourceFile/TemplateFile/datafile_template.xls', '../DataFiles/' + filename)
        except IOError as e:
            logging.critical("Unable to copy template file. %s" % e)
            print("Unable to copy template file. %s" % e)
            exit(1)
        file = xlrd.open_workbook('../DataFiles/' + filename)

    file = xlrd.open_workbook('../DataFiles/' + filename)
    datafile = copy(file)
    sheet = datafile.get_sheet(num_sheet)       #选取待写sheet
    for i in range(len(data_split)):
        data = data_split[i].replace('"', '')
        data = data.split(':', 1)
        # sheet.write(0, i, data[0])            #写入字段
        sheet.write(writerow, i, data[1])       #写入内容

    try:                                                                #保存写入数据
        datafile.save('../DataFiles/' + filename) #存储
    except IOError as e:
        logging.info("Unable to save file. %s" % e)                    #写入日志
        print("Unable to save file. %s" % e)    #报错
        print("Please close file " + filename + '\n')
        # exit(1)                                 #退出程序，否则将一直运行
    return


if __name__ == "__main__":
    f = open('../SourceFile/HttpPackageFile/postconfig.txt')
    http_package = f.read()
    data_package = extra_data(http_package)
    print(data_package)
    for i in range(5):
        save_data(data_package)
    # print(get_filename())
    # filename = get_filename()
    # try:
    #     file = xlrd.open_workbook('DataFiles/' + filename)
    # except IOError:
    #     try:
    #         copyfile('datafile_template.xls', 'DataFiles/' + filename)
    #     except IOError as e:
    #         print("Unable to copy template file. %s" % e)
    #     file = file = xlrd.open_workbook('DataFiles/' + filename)
