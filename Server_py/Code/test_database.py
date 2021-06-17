import sqlite3
list_name = ("postconfig_keyword", "realdata_keyword", "recycledata_keyword")

postconfig_keyword = ("time", "id", "devicesn", "height", "addtionheight", "smallwidth1", "smallwidth2", "bigwidth", "rate", "deviceno", "channelno", "alertcollision", "alarmcollision", "minheight", "maxheight",
                      "minmargin", "maxmargin", "alertwind", "alarmwind", "alertweight", "alarmweight", "alertelevation", "alarmelevation", "gpsx", "gpsy", "deviceiccid", "devkey", "mincycletime", "mincycleweight",
                      "model", "version")

realdata_keyword = ("time", "id", "sendTime", "height", "angle", "extent", "weight", "weightPer", "force", "forcePer", "wind", "state", "obliqueX", "obliqueY", "alertalarm", "maxweight", "obliuqePer", "windPer")

recycledata_keyword = ("time", "id", "sendTime", "maxHeight", "minHeight", "startHeight", "endHeight", "maxWeight", "maxWeightPer", "startTime", "endTime", "maxForce", "maxForcePer", "sAngle", "eAngle", "sExtent",
                       "maxElevation", "minElevation", "status", "alertalarm")

def DB_Initial():
    # DB_name = "test"
    con = sqlite3.connect("../DataBase/test.db")  # 连接数据库
    cur = con.cursor()  # 创建游标

    keyword = str(postconfig_keyword)
    keyword = keyword.replace(' ', '')
    keyword = keyword.replace('\'', '')
    sql = "CREATE TABLE IF NOT EXISTS " + "postconfig" + keyword
    cur.execute(sql)

    keyword = str(realdata_keyword)
    keyword = keyword.replace(' ', '')
    keyword = keyword.replace('\'', '')
    sql = "CREATE TABLE IF NOT EXISTS " + "realdata" + keyword
    cur.execute(sql)

    keyword = str(recycledata_keyword)
    keyword = keyword.replace(' ', '')
    keyword = keyword.replace('\'', '')
    sql = "CREATE TABLE IF NOT EXISTS " + "recycledata" + keyword
    cur.execute(sql)

def package_decode_DB(data_package):        #解码data_package，以便直接写入数据库
    this_type = data_package[0]
    data_split = data_package.copy()  # copy list  python的传址传值调用特性  可变对象传址调用 不可变对象传址调用
    # data_split.remove(this_type)              #去头，只留字段与内容
    try:
        data_split.remove('')  # 去掉空数据      data_split:分割后的数据
    except ValueError as e:
        data_split.remove(this_type)  # 去头，只留字段与内容
    else:
        data_split.remove(this_type)

    # print(data_split)
    for i in range(len(data_split)):
        data = data_split[i].replace('"', '')
        data = data.split(':', 1)
        data_split[i] = data[1]

    data_split.insert(0, this_type)
    return data_split

def DB_writedata(data_decode):      #输入由package_decode_DB得到的解码data，写入数据库
    list_name = data_decode[0]       #头部信息 表民
    data = data_decode[1:len(data_decode)]        #余下信息 可以直接写入的数据
    con = sqlite3.connect("../DataBase/test.db")        #连接数据库
    cur = con.cursor()      #创建游标
    sql = "INSERT INTO " + list_name + " values(" + (len(data)-1)*"?," + "?" + ")"
    cur.execute(sql,data)
    con.commit()
    cur.close()


if __name__ == "__main__":
    con = sqlite3.connect("../DataBase/test.db")        #连接数据库
    cur = con.cursor()      #创建游标
    # sql = "INSERT INTO postconfig values(?,?,?)"
    # sql = "INSERT INTO test values(?,?,?)"
    # data = (11, "zgq", 20)
    sql = "INSERT INTO postconfig values(" + 30*"?," + "?" + ")"
    data = range(31)
    print(data)
    cur.execute(sql,data)
    con.commit()
    cur.close()

    # sql = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
    # cur.execute(sql)
    # # sql = "INSERT INTO test values(?,?,?)", (6, "zgq", 20)
    # cur.execute("INSERT INTO test values(?,?,?)", (8, "zgq", 20))
    # cur.execute("INSERT INTO test values(?,?,?)", (9, "zgq", 20))
    # cur.execute("INSERT INTO test values(?,?,?)", (10, "zgq", 20))
    # con.commit()
    # cur.close()
    # con.close()

    # con = sqlite3.connect("../DataBase/test.db")        #连接数据库
    # cur = con.cursor()      #创建游标
    # sql = "CREATE TABLE IF NOT EXISTS test(%s)"%

    # DB_name = "test1"
    #
    # keyword = str(postconfig_keyword)
    # keyword = keyword.replace(' ', '')
    # keyword = keyword.replace('\'', '')
    #
    # sql = "CREATE TABLE IF NOT EXISTS " + DB_name + keyword
    #
    # con = sqlite3.connect("../DataBase/test.db")        #连接数据库
    # cur = con.cursor()      #创建游标
    # cur.execute(sql)
    DB_Initial()
    # print(sql)

