import redis,json

rc = redis.Redis(host='118.24.3.40',password='HK139bc&*',port=6379,db=0,decode_responses=True)


def get_all(rc, key, block=True, timeout=None):
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


def keys(self):
    keys = rc.keys()

    return keys


def iskey(rc, key):
    if rc.exists(key):

        return 1

    else:

        return 0


def get(rc, key):
    res = rc.get(key)

    nres = json.loads(res)

    return nres


def put(rc, key, value):
    new_value = json.dumps(value)
    res = rc.set(key, new_value)