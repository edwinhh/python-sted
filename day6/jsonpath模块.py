import jsonpath
d = {
        "error_code": 0,
        "stu_info": [
                {
                        "id": 314,
                        "name": "矿泉水",
                        "sex": "男",
                        "age": 18,
                        "addr": "北京市昌平区",
                        "grade": "摩羯座",
                        "phone": "18317155663",
                        "gold": 14405
                },
            {
                "id": 314,
                "name": "矿泉水",
                "sex": "男",
                "age": 18,
                "addr": "北京市昌平区",
                "grade": "摩羯座",
                "phone": "18317155664",
                "gold": 14405
            }
            
        ]}
result = jsonpath.jsonpath(d,'$.stu_info[0].id')
result = jsonpath.jsonpath(d,'$..id')
print(result)