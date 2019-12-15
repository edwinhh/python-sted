#coding:utf-8
import flask
from flask_cors import CORS

server = flask.Flask(__name__)
CORS(server, supports_credentials=True)

server.config['JSON_AS_ASCII'] = False


@server.route("/api/project", methods=["get", "put", "post", "delete"])
def project():
    print(flask.request.args)
    if flask.request.method == "GET":
        data = {"code": 0, "msg": "操作成功", "data": [{"id": 2, "create_time": "2019-11-13 10:42:38", "name": "测试本机项目", "desc": "测试本机项目", "user": "dsx", "host": "http://127.0.0.1:8000"}, {"id": 1, "create_time": "2019-11-12 22:02:04", "name": "金桔宝", "desc": "金桔宝", "user": "dsx", "host": "127.0.0.1:8080"}], "count": 2}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/parameter", methods=["get", "put", "post", "delete"])
def parameter():
    print(flask.request.args)
    if flask.request.method == "GET":
        data = {"code": 0, "msg": "操作成功", "data": [{"id": 5, "name": "username", "desc": "用户名", "value": "dsx"}, {"id": 4, "name": "测试", "desc": "测试", "value": "123"}], "count": 2}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/interface", methods=["get", "put", "post", "delete"])
def interface():
    print(flask.request.values)
    if flask.request.method == "GET":
        data = {"code": 0, "msg": "操作成功", "data": [{"id": 4, "create_time": "2019-11-13 12:21:48", "update_time": "2019-11-13 12:21:48", "name": "获取参数接口", "uri": "/api/parameter", "params": None, "headers": "{\"token\":\"${token}\"}", "project_id": 2, "user": "dsx", "project": "测试本机项目"}, {"id": 3, "create_time": "2019-11-13 10:49:04", "update_time": "2019-11-13 10:49:04", "name": "项目接口", "uri": "/api/project", "params": None, "headers": "{\"token\":\"${token}\"}", "project_id": 2, "user": "dsx", "project": "测试本机项目"}, {"id": 2, "create_time": "2019-11-13 10:43:20", "update_time": "2019-11-13 10:43:20", "name": "登录接口", "uri": "/api/login", "params": None, "headers": None, "project_id": 2, "user": "dsx", "project": "测试本机项目"}, {"id": 1, "create_time": "2019-11-12 22:02:35", "update_time": "2019-11-12 22:02:35", "name": "接口名称", "uri": "/api/login", "params": "{\"key\":\"1\"}", "headers": "{\"key1\":\"value1\"}", "project_id": 1, "user": "dsx", "project": "金桔宝"}], "count": 4}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/case_collection", methods=["get", "put", "post", "delete"])
def case_collection():
    print(flask.request.values)
    if flask.request.method == "GET":
        data = {"code": 0, "msg": "操作成功", "data": [
            {"id": 1, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 2, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 3, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 4, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 5, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 6, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 7, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 8, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3},
            {"id": 9, "create_time": "2019-11-13 12:06:51", "update_time": "2019-11-13 12:06:51", "name": "本机集合13",
             "desc": "本机集合", "project_id": 2, "user": "dsx", "report_batch": "63640cae-deef-49d6-8d50-30edff146705",
             "status": 3, "project_name": "测试本机项目", "case_count": 3}], "count": 9}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/run", methods=["post"])
def case_run():
    data = {
        "code": 0,
        "msg": "成功"
    }
    return flask.jsonify(data)

@server.route("/api/run_collection", methods=["post"])
def run_collection():
    data = {
        "code": 0,
        "msg": "成功"
    }
    return flask.jsonify(data)

@server.route("/api/case", methods=["get", "put", "post", "delete"])
def case():
    print(flask.request.values)
    if flask.request.method == "GET":
        data = {"code": 0, "msg": "操作成功", "data": [{"id": 8, "create_time": "2019-11-13 17:01:16", "update_time": "2019-11-13 17:01:16", "title": "测试", "project_id": 2, "interface_id": 4, "user": "dsx", "method": 1, "cache_field": "123,456", "check": "123", "params": None, "headers": None, "is_json": False, "json": None, "status": 2, "report_batch": None, "project_name": "测试本机项目", "interface_name": "/api/parameter", "rely_case": []}, {"id": 6, "create_time": "2019-11-13 15:40:43", "update_time": "2019-11-13 15:40:43", "title": "创建参数", "project_id": 2, "interface_id": 4, "user": "dsx", "method": 1, "cache_field": None, "check": "123", "params": "{\"name\":\"测试\",\"desc\":\"测试\",\"value\":\"123\"}", "headers": None, "is_json": False, "json": None, "status": 999, "report_batch": "71cd8d7d-f18a-46b6-b871-bbc159863883", "project_name": "测试本机项目", "interface_name": "/api/parameter", "rely_case": []}, {"id": 5, "create_time": "2019-11-13 12:33:07", "update_time": "2019-11-13 12:33:07", "title": "参数请求", "project_id": 2, "interface_id": 4, "user": "dsx", "method": 2, "cache_field": "id", "check": "code=0", "params": "{\"project_id\":\"2\"}", "headers": None, "is_json": False, "json": None, "status": 1, "report_batch": "cf9c57e5-eba0-4be9-b0c2-6d08002d2130", "project_name": "测试本机项目", "interface_name": "/api/parameter", "rely_case": [{"id": 4, "title": "项目请求"}]}, {"id": 4, "create_time": "2019-11-13 10:49:39", "update_time": "2019-11-13 10:49:39", "title": "项目请求", "project_id": 2, "interface_id": 3, "user": "dsx", "method": 2, "cache_field": None, "check": "code=0", "params": None, "headers": None, "is_json": False, "json": None, "status": 1, "report_batch": "c1440343-89aa-46a1-8fe8-7740b35ce854", "project_name": "测试本机项目", "interface_name": "/api/project", "rely_case": [{"id": 3, "title": "本机登录"}]}, {"id": 3, "create_time": "2019-11-13 10:44:33", "update_time": "2019-11-13 10:44:33", "title": "本机登录", "project_id": 2, "interface_id": 2, "user": "dsx", "method": 1, "cache_field": "token", "check": "code=0", "params": "{\"username\":\"17610105018\",\"password\":\"123456\"}", "headers": None, "is_json": False, "json": None, "status": 1, "report_batch": "50154aa1-335c-42f8-a224-f7d7819eae35", "project_name": "测试本机项目", "interface_name": "/api/login", "rely_case": []}, {"id": 2, "create_time": "2019-11-13 00:11:03", "update_time": "2019-11-13 00:11:03", "title": "test2", "project_id": 1, "interface_id": 1, "user": "dsx", "method": 1, "cache_field": None, "check": "1", "params": None, "headers": None, "is_json": False, "json": None, "status": 2, "report_batch": None, "project_name": "金桔宝", "interface_name": "/api/login", "rely_case": [{"id": 1, "title": "登录用例"}]}, {"id": 1, "create_time": "2019-11-12 22:03:13", "update_time": "2019-11-12 22:03:13", "title": "登录用例", "project_id": 1, "interface_id": 1, "user": "dsx", "method": 1, "cache_field": None, "check": "1", "params": None, "headers": None, "is_json": False, "json": None, "status": 2, "report_batch": None, "project_name": "金桔宝", "interface_name": "/api/login", "rely_case": []}], "count": 7}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/join_case", methods=["post", "get"])
def join_case():
    print(flask.request.values)
    if flask.request.method == "GET":
        data = {"code": 0, "msg": "操作成功", "data": {
            "all_case": [{"id": 8, "title": "测试"}, {"id": 6, "title": "创建参数"}, {"id": 5, "title": "参数请求"},
                         {"id": 4, "title": "项目请求"}, {"id": 3, "title": "本机登录"}], "join_case": [5, 4, 3]}}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


# @server.route("/api/case_response", methods=["get"])
# def case_response():
#     print(flask.request.values)
#     if flask.request.method == "GET":
#
#         data = {
#             "code": 0,
#             "msg": "成功",
#             "data": {
#                 "all_case": [{"id": 1, "name": "登陆用例", "create_time": "2019-07-21 18:01:02",
#                               "update_time": "2019-07-21 18:01:02",
#                               "project_name": "牛牛测试项目1", "response": "回归流程使用", "case_count": 5,
#                               "report_id": 1,
#                               "report_name": "2019-08-06测试报告", "user": "牛牛"},
#                              {"id": 2, "name": "登陆用例1", "create_time": "2019-07-21 18:01:02",
#                               "update_time": "2019-07-21 18:01:02",
#                               "project_name": "牛牛测试项目2", "project_id": 2, "desc": "冒烟测试使用", "case_count": 4,
#                               "report_id": 2,
#                               "report_name": "2019-08-06测试报告", "user": "牛牛"},
#                              {"id": 3, "name": "登陆用例2", "create_time": "2019-07-21 18:01:02",
#                               "update_time": "2019-07-21 18:01:02",
#                               "project_name": "牛牛测试项目3", "project_id": 3, "desc": "支付流程", "case_count": 3,
#                               "report_id": 3,
#                               "report_name": "2019-08-06测试报告", "user": "牛牛"}],
#                 "join_case": [1]
#
#             }
#         }
#     else:
#         data = {
#             "code": 0,
#             "msg": "成功"
#         }
#     return flask.jsonify(data)


@server.route("/api/login", methods=["post"])
def login():
    data = {
        "code": 0,
        "msg": "成功",
        "token": "token1234355",
        "user": "牛牛"
    }
    return flask.jsonify(data)


@server.route("/api/logout", methods=['get'])
def logout():
    data = {
        "code": 0,
        "msg": "成功"
    }
    return flask.jsonify(data)


@server.route("/api/report", methods=['get'])
def report():
    data = {"code": 0, "msg": "操作成功", "data": [{"id": 145, "create_time": "2019-11-23 12:53:34", "update_time": "2019-11-23 12:53:34", "url": "http://127.0.0.1:8000/api/parameter", "project": 2, "title": "参数请求", "params": "{\"project_id\": \"2\"}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 5, 'name': 'username', 'desc': '用户名', 'value': 'dsx'}, {'id': 4, 'name': '测试', 'desc': '测试', 'value': '123'}], 'count': 2}", "case": 5, "case_collection": "本机集合13", "batch": "111e8fa4-4407-44cf-97f7-ee9a2cd1b9b2", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-23 12:53:34", "check": "code=0", "method": "GET"}, {"id": 144, "create_time": "2019-11-23 12:53:32", "update_time": "2019-11-23 12:53:32", "url": "http://127.0.0.1:8000/api/project", "project": 2, "title": "项目请求", "params": "{}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 2, 'create_time': '2019-11-13 10:42:38', 'name': '测试本机项目', 'desc': '测试本机项目', 'user': 'dsx', 'host': 'http://127.0.0.1:8000'}, {'id': 1, 'create_time': '2019-11-12 22:02:04', 'name': '金桔宝', 'desc': '金桔宝', 'user': 'dsx', 'host': '127.0.0.1:8080'}], 'count': 2}", "case": 4, "case_collection": "本机集合13", "batch": "111e8fa4-4407-44cf-97f7-ee9a2cd1b9b2", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-23 12:53:32", "check": "code=0", "method": "GET"}, {"id": 143, "create_time": "2019-11-23 12:53:31", "update_time": "2019-11-23 12:53:31", "url": "http://127.0.0.1:8000/api/login", "project": 2, "title": "本机登录", "params": "{\"username\": \"17610105018\", \"password\": \"123456\"}", "response": "{'code': 0, 'msg': '操作成功', 'token': '783d2c6ded55ca4f5bb865923ff29cbc', 'user': 'dsx', 'user_id': 1}", "case": 3, "case_collection": "本机集合13", "batch": "111e8fa4-4407-44cf-97f7-ee9a2cd1b9b2", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-23 12:53:31", "check": "code=0", "method": "POST"}, {"id": 142, "create_time": "2019-11-23 12:53:09", "update_time": "2019-11-23 12:53:09", "url": "http://127.0.0.1:8000/api/parameter", "project": 2, "title": "创建参数", "params": "{\"name\": \"\\u6d4b\\u8bd5\", \"desc\": \"\\u6d4b\\u8bd5\", \"value\": \"123\"}", "response": "{'code': -1, 'msg': 'name具有 参数名称 的 全局参数表 已存在。'}", "case": 6, "case_collection": "单用例运行", "batch": "71cd8d7d-f18a-46b6-b871-bbc159863883", "reason": "校验点写法出错", "duration": 100, "status": 999, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-23 12:53:09", "check": "123", "method": "POST"}, {"id": 141, "create_time": "2019-11-23 12:53:04", "update_time": "2019-11-23 12:53:04", "url": "http://127.0.0.1:8000/api/login", "project": 2, "title": "本机登录", "params": "{\"username\": \"17610105018\", \"password\": \"123456\"}", "response": "{'code': 0, 'msg': '操作成功', 'token': 'cc0c3eb41b9b6be9b01d726523dcf1b9', 'user': 'dsx', 'user_id': 1}", "case": 3, "case_collection": "单用例运行", "batch": "50154aa1-335c-42f8-a224-f7d7819eae35", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-23 12:53:04", "check": "code=0", "method": "POST"}, {"id": 140, "create_time": "2019-11-23 12:51:34", "update_time": "2019-11-23 12:51:34", "url": "http://127.0.0.1:8000/api/login", "project": 2, "title": "本机登录", "params": "{\"username\": \"17610105018\", \"password\": \"123456\"}", "response": "{'code': 0, 'msg': '操作成功', 'token': '8d2bba744a35f76b0ea99ccc296feff4', 'user': 'dsx', 'user_id': 1}", "case": 3, "case_collection": "单用例运行", "batch": "999c5990-6bd3-406f-8750-3b1b9a16ec50", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-23 12:51:34", "check": "code=0", "method": "POST"}, {"id": 139, "create_time": "2019-11-23 12:50:51", "update_time": "2019-11-23 12:50:51", "url": "http://127.0.0.1:8080/api/login", "project": 2, "title": "本机登录", "params": "{\"username\": \"17610105018\", \"password\": \"123456\"}", "response": "{'msg': \"请求接口出错，http://127.0.0.1:8080/api/login,HTTPConnectionPool(host='127.0.0.1', port=8080): Max retries exceeded with url: /api/login (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x10555d860>: Failed to establish a new connection: [Errno 61] Connection refused',))\"}", "case": 3, "case_collection": "单用例运行", "batch": "753a6a27-98d7-42c6-b244-8096b53ce38c", "reason": "code和预期结果不一致，预期结果【0】，实际结果【空】,运算符【=】", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-23 12:50:51", "check": "code=0", "method": "POST"}, {"id": 138, "create_time": "2019-11-15 16:21:56", "update_time": "2019-11-15 16:21:56", "url": "http://127.0.0.1:8080/api/project", "project": 2, "title": "项目请求", "params": "{}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 2, 'create_time': '2019-11-13 10:42:38', 'name': '测试本机项目', 'desc': '测试本机项目', 'user': 'dsx', 'host': 'http://127.0.0.1:8080'}, {'id': 1, 'create_time': '2019-11-12 22:02:04', 'name': '金桔宝', 'desc': '金桔宝', 'user': 'dsx', 'host': '127.0.0.1:8080'}], 'count': 2}", "case": 4, "case_collection": "单用例运行", "batch": "c1440343-89aa-46a1-8fe8-7740b35ce854", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-15 16:21:56", "check": "code=0", "method": "GET"}, {"id": 137, "create_time": "2019-11-15 16:21:54", "update_time": "2019-11-15 16:21:54", "url": "http://127.0.0.1:8080/api/login", "project": 2, "title": "本机登录", "params": "{\"username\": \"17610105018\", \"password\": \"123456\"}", "response": "{'code': 0, 'msg': '操作成功', 'token': '1c9d51ccae8e7606ab5cc2c22a48650e', 'user': 'dsx', 'user_id': 1}", "case": 3, "case_collection": "单用例运行", "batch": "c1440343-89aa-46a1-8fe8-7740b35ce854", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-15 16:21:54", "check": "code=0", "method": "POST"}, {"id": 136, "create_time": "2019-11-15 16:21:42", "update_time": "2019-11-15 16:21:42", "url": "http://127.0.0.1:8080/api/parameter", "project": 2, "title": "创建参数", "params": "{\"name\": \"\\u6d4b\\u8bd5\", \"desc\": \"\\u6d4b\\u8bd5\", \"value\": \"123\"}", "response": "{'code': -2, 'msg': '请登录！'}", "case": 6, "case_collection": "单用例运行", "batch": "359810f9-9e16-40a2-81b4-e010c4db9e44", "reason": "校验点写法出错", "duration": 100, "status": 999, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-15 16:21:42", "check": "123", "method": "POST"}, {"id": 135, "create_time": "2019-11-13 18:15:37", "update_time": "2019-11-13 18:15:37", "url": "http://127.0.0.1:8080/api/parameter", "project": 2, "title": "创建参数", "params": "{\"name\": \"\\u6d4b\\u8bd5\", \"desc\": \"\\u6d4b\\u8bd5\", \"value\": \"123\"}", "response": "{'code': -1, 'msg': 'name具有 参数名称 的 全局参数表 已存在。'}", "case": 6, "case_collection": "单用例运行", "batch": "b2a61952-88ed-43d4-b43a-b847a69ba82b", "reason": "校验点写法出错", "duration": 100, "status": 999, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 18:15:37", "check": "123", "method": "POST"}, {"id": 134, "create_time": "2019-11-13 18:14:55", "update_time": "2019-11-13 18:14:55", "url": "http://127.0.0.1:8080/api/parameter", "project": 2, "title": "创建参数", "params": "{\"name\": \"\\u6d4b\\u8bd5\", \"desc\": \"\\u6d4b\\u8bd5\", \"value\": \"123\"}", "response": "{'code': -1, 'msg': 'name具有 参数名称 的 全局参数表 已存在。'}", "case": 6, "case_collection": "单用例运行", "batch": "42677205-d36a-4792-8b17-7ca71960e4bc", "reason": "校验点写法出错", "duration": 100, "status": 999, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 18:14:55", "check": "123", "method": "POST"}, {"id": 133, "create_time": "2019-11-13 18:12:10", "update_time": "2019-11-13 18:12:10", "url": "http://127.0.0.1:8080/api/parameter", "project": 2, "title": "创建参数", "params": "{\"name\": \"\\u6d4b\\u8bd5\", \"desc\": \"\\u6d4b\\u8bd5\", \"value\": \"123\"}", "response": "{'code': -1, 'msg': 'name具有 参数名称 的 全局参数表 已存在。'}", "case": 6, "case_collection": "单用例运行", "batch": "c19a3b82-e1f7-4bb4-b87f-4520c1590073", "reason": "验证通过", "duration": 100, "status": 999, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 18:12:10", "check": "123", "method": "POST"}, {"id": 132, "create_time": "2019-11-13 17:29:58", "update_time": "2019-11-13 17:29:58", "url": "http://127.0.0.1:8080/api/parameter", "project": 2, "title": "参数请求", "params": "{\"project_id\": \"2\"}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 4, 'name': '测试', 'desc': '测试', 'value': '123'}], 'count': 1}", "case": 5, "case_collection": "单用例运行", "batch": "cf9c57e5-eba0-4be9-b0c2-6d08002d2130", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 17:29:58", "check": "code=0", "method": "GET"}, {"id": 131, "create_time": "2019-11-13 17:29:57", "update_time": "2019-11-13 17:29:57", "url": "http://127.0.0.1:8080/api/project", "project": 2, "title": "项目请求", "params": "{}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 2, 'create_time': '2019-11-13 10:42:38', 'name': '测试本机项目', 'desc': '测试本机项目', 'user': 'dsx', 'host': 'http://127.0.0.1:8080'}, {'id': 1, 'create_time': '2019-11-12 22:02:04', 'name': '金桔宝', 'desc': '金桔宝', 'user': 'dsx', 'host': '127.0.0.1:8080'}], 'count': 2}", "case": 4, "case_collection": "单用例运行", "batch": "cf9c57e5-eba0-4be9-b0c2-6d08002d2130", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 17:29:57", "check": "code=0", "method": "GET"}, {"id": 130, "create_time": "2019-11-13 17:29:55", "update_time": "2019-11-13 17:29:55", "url": "http://127.0.0.1:8080/api/login", "project": 2, "title": "本机登录", "params": "{\"username\": \"17610105018\", \"password\": \"123456\"}", "response": "{'code': 0, 'msg': '操作成功', 'token': 'd91da70a2394669cdc0e7bef4a5ec222', 'user': 'dsx', 'user_id': 1}", "case": 3, "case_collection": "单用例运行", "batch": "cf9c57e5-eba0-4be9-b0c2-6d08002d2130", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 17:29:55", "check": "code=0", "method": "POST"}, {"id": 129, "create_time": "2019-11-13 17:29:28", "update_time": "2019-11-13 17:29:28", "url": "http://127.0.0.1:8080/api/project", "project": 2, "title": "项目请求", "params": "{}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 2, 'create_time': '2019-11-13 10:42:38', 'name': '测试本机项目', 'desc': '测试本机项目', 'user': 'dsx', 'host': 'http://127.0.0.1:8080'}, {'id': 1, 'create_time': '2019-11-12 22:02:04', 'name': '金桔宝', 'desc': '金桔宝', 'user': 'dsx', 'host': '127.0.0.1:8080'}], 'count': 2}", "case": 4, "case_collection": "单用例运行", "batch": "1d10fdaa-698b-4fef-a8a8-59e53576f5ae", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 17:29:28", "check": "code=0", "method": "GET"}, {"id": 128, "create_time": "2019-11-13 17:29:27", "update_time": "2019-11-13 17:29:27", "url": "http://127.0.0.1:8080/api/login", "project": 2, "title": "本机登录", "params": "{\"username\": \"17610105018\", \"password\": \"123456\"}", "response": "{'code': 0, 'msg': '操作成功', 'token': 'd5e84d54c497e74a746ffeaa061cc28e', 'user': 'dsx', 'user_id': 1}", "case": 3, "case_collection": "单用例运行", "batch": "1d10fdaa-698b-4fef-a8a8-59e53576f5ae", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 17:29:27", "check": "code=0", "method": "POST"}, {"id": 127, "create_time": "2019-11-13 17:29:20", "update_time": "2019-11-13 17:29:20", "url": "http://127.0.0.1:8080/api/parameter", "project": 2, "title": "创建参数", "params": "{\"name\": \"\\u6d4b\\u8bd5\", \"desc\": \"\\u6d4b\\u8bd5\", \"value\": \"123\"}", "response": "{'code': -1, 'msg': 'name具有 参数名称 的 全局参数表 已存在。'}", "case": 6, "case_collection": "单用例运行", "batch": "a64261bd-c5d3-4b18-8c61-a549e7be29c6", "reason": "code和预期结果不一致，预期结果【0】，实际结果【-1】,运算符【=】", "duration": 100, "status": 999, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 17:29:20", "check": "123", "method": "POST"}, {"id": 126, "create_time": "2019-11-13 17:28:16", "update_time": "2019-11-13 17:28:16", "url": "http://127.0.0.1:8080/api/project", "project": 2, "title": "项目请求", "params": "{}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 2, 'create_time': '2019-11-13 10:42:38', 'name': '测试本机项目', 'desc': '测试本机项目', 'user': 'dsx', 'host': 'http://127.0.0.1:8080'}, {'id': 1, 'create_time': '2019-11-12 22:02:04', 'name': '金桔宝', 'desc': '金桔宝', 'user': 'dsx', 'host': '127.0.0.1:8080'}], 'count': 2}", "case": 4, "case_collection": "本机集合13", "batch": "117ebcf4-fdec-4ebc-a9b4-5628f4b79abb", "reason": "验证通过", "duration": 100, "status": 1, "user": 1, "project_name": "测试本机项目", "run_user": "dsx", "run_time": "2019-11-13 17:28:16", "check": "code=0", "method": "GET"}], "count": 145}
    return flask.jsonify(data)


@server.route("/api/collection_report", methods=['get'])
def collection_report():
    data = {"code": 0, "msg": "操作成功", "data": {"case_collection": "本机集合13", "run_time": "2019-12-05 15:27:21", "case_count": 1, "pass_count": 1, "run_user": "dsx", "fail_count": 0, "duration": 100, "report_batch": "e714e8d1-477e-4851-b76a-b57cbd575af7"}}

    return flask.jsonify(data)


@server.route("/api/case_report", methods=['get'])
def case_report():
    data = {"code": 0, "msg": "操作成功", "data": {"title": "参数请求", "run_time": "2019-11-13 17:29:58", "project_name": "测试本机项目", "status": 1, "case_collection": "单用例运行", "duration": 100, "run_user": "dsx", "url": "http://127.0.0.1:8080/api/parameter", "method": 2, "check": "code=0", "reason": "验证通过", "params": "{\"project_id\": \"2\"}", "response": "{'code': 0, 'msg': '操作成功', 'data': [{'id': 4, 'name': '测试', 'desc': '测试', 'value': '123'}], 'count': 1}"}}
    return flask.jsonify(data)


@server.route("/api/dataInfo", methods=['get'])
def dataInfo():
    data = {
        "code": 0,
        "msg": "成功",
        "data": {"project": 128, "interface": 100, "case_join": 100, "caseNum": 100,
                 "info": {"caseNumInfo": [80, 4.9, 7, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20, 6.4, 3.3],
                          "runInfo": [2.6, 5.9, 9, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6, 2.3],
                          "passInfo": [2, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23, 16.5, 12, 6.2]}}
    }

    return flask.jsonify(data)


@server.route("/api/test", methods=['get'])
def test():
    data = {
        "code": 0,
        "msg": "成功",
        "data": [
            {"id": 1, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 2, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 3, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 4, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 5, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 5, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 6, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 7, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 8, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 9, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 10, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 11, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 12, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 13, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 14, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 15, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 16, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 17, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 18, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 19, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 20, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
            {"id": 21, "date": "2016-05-03", "user": "王小虎", "interface": "登录", "project": "南京银行", "report": "查看",
             "status": "失败", "title": "登录1"},
        ],
        "count": 21
    }

    return flask.jsonify(data)


server.run("127.0.0.1", port=8080, debug=True)
