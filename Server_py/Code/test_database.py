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

if __name__ == "__main__":
    # con = sqlite3.connect("../DataBase/test.db")        #连接数据库
    # cur = con.cursor()      #创建游标
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

