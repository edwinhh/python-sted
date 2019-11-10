import time

import pymysql,hashlib,redis

def op_mysql(sql,many=True):
    db_info = {'user': 'jxz', 'password': '123456',
            'host': '118.24.3.40', 'db': 'jxz', 'port': 3306, 'charset': 'utf8',
            'autocommit': True}
    try:
        conn = pymysql.connect(**db_info)  # 建立连接
    except Exception as e:
        print("mysql连接失败",e)
        return False
    cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标
    try:
        cur.execute(sql)  # 执行sql语句，insert 、update 、delete
    except Exception as e:
        print("sql错误，%s"%sql)
        result = "sql错误,%s"%sql
    else:
        if many:
            result = cur.fetchall()
        else:
            result = cur.fetchone() # {''}
    finally:
        cur.close()
        conn.close()
    return result

def md5(s,salt=''):
    new_s = str(s) + salt
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()

def my_redis(k,v=None,expire=60*60*2):
    r = redis.Redis(host='118.24.3.40', password='HK139bc&*', port=6379, db=0, decode_responses=True)
    if v:
        r.set(k,v,expire)
    else:
        result = r.get(k)
        return result

def get_sessionid(username):
    sessionid = '%s%s'%(username,time.time())
    new_sessionid = md5(sessionid,'@#F@#fdsf')
    return new_sessionid

# def is_price(s):
#     s = str(s)
#     if s.isdigit():
#         return True
#     if s.count('.') == 1:
#         left, right = s.split('.')
#         if left.isdigit() and right.isdigit():
#             return True
#     return False

def is_price(s):
    try:
        price = float(s)
    except Exception as e:
        print("价格错误")
        return False
    return price

def get_redis():
    return redis.Redis(host='118.24.3.40', password='HK139bc&*', port=6379, db=0, decode_responses=True)
