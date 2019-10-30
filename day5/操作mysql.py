import pymysql
ip ="118.24.3.40"
user = 'jxz'
password="123456"
db='jxz'
port=3306
charset='utf8'
conn = pymysql.connect(host=ip,user=user,password=password,
                       db=db,port=port,charset=charset,autocommit=True)#建立连接

cur = conn.cursor(pymysql.cursors.DictCursor) #游标

sql = 'select * from app_myuser limit 5;'

cur.execute(sql)#执行sql语句，insert 、update 、delete
#conn.commit() #提交
all = cur.fetchall()
# one = cur.fetchone()
# many = cur.fetchmany(2)
cur.close()
conn.close()

# print(one)
# print(many)
print(all)


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



op_mysql('sdfsdf') #user=jxz,password=123456



"""
create table mjz (id int unique not null, name varchar(20) not null, phone varchar(11) unique not null);
insert into mjz (id,name,phone) values (1,"小白","19812343211");

insert into mjz (id,name,phone) values (2,"小白2","17812343211");
update mjz set name="春光" where id =1;
delete from mjz where id=3;
"""