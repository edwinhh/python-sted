import pymysql

def op_mysql(sql):
    db_info = {'user': 'jxz', 'password': '123456',
            'host': '118.24.3.40', 'db': 'jxz', 'port': 3306, 'charset': 'utf8',
            'autocommit': True}
    conn = pymysql.connect(**db_info)  # 建立连接
    cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标
    cur.execute(sql)  # 执行sql语句，insert 、update 、delete
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
sql="select * from app_myuser"