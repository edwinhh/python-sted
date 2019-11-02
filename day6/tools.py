import pymysql,hashlib,redis,json


def op_mysql(sql,many=True):
    db_info = {'user': 'jxz', 'password': '123456',
            'host': '118.24.3.40', 'db': 'jxz', 'port': 3306, 'charset': 'utf8',
            'autocommit': True}
    conn = pymysql.connect(**db_info)  # 建立连接
    cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标
    cur.execute(sql)  # 执行sql语句，insert 、update 、delete
    if many:
        result = cur.fetchall()
    else:
        result = cur.fetchone() # {''}
    cur.close()
    conn.close()
    return result

# username='hh'
# money=1
# sql1 = 'SELECT balance FROM user WHERE username="%s"'%(username)
# balance=op_mysql(sql1,many=0)
# print(balance)
# sql2='update user set balance=%s-%s where username="%s";' %(float(balance.get("balance")),float(money),username)
# print(sql2)
# op_mysql(sql2, many=0)


def md5(s,salt=''):
    new_s = str(s) + salt
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()
s="3"

def isdigit(s):
    try:
        return float(s)

    except:
        return 0



rc = redis.Redis(host='118.24.3.40',password='HK139bc&*',port=6379,db=0,decode_responses=True)
def get_all(key, block=True, timeout=None):
    for i in rc.keys():

        if key in str(i):

            type = rc.type(i)

            if type == 'string':

                vals = rc.get(i)

            elif type == 'list':

                vals = rc.lrange(i, 0, -1)

            elif type == 'set':

                vals = rc.smembers(i)

            elif type == 'zset':

                vals = rc.zrange(i, 0, -1)

            elif type == "hash":
                vals = rc.hgetall(i)

            else:

                print(type, i)

    return list(vals[0])


def keys():
    keys = rc.keys()

    return keys


def iskey(key):
    if rc.exists(key):

        return 1
    else:
        return 0


def get(key):
    res = rc.get(key)
    nres = json.loads(res)
    return nres


def put(key, value):
    new_value = json.dumps(value)
    res = rc.set(key, new_value)

#rc.hset('user_seesions', '1102a245b59af9c783bb8c18948ef96d',"{'user_name':'wyj','userid':1}")
# a=rc.get('68430f09c4db0e7b193226551dc4af16')
# a2=rc.get('f3504b520f1de9885ba7ac58f68e32a3')
# print(a)
# print(a2)