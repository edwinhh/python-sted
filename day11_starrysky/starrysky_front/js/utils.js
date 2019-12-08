function get_token() {
    //获取token
    let token = localStorage.getItem('token');
    if (token == null) {
        layer.alert("登录信息已经失效，点击确定跳转登陆页面，取消保留当前页面", function () {
            top.window.location.href = 'login.html';

        })
    }

    return token

}

function set_user(userId, user) {
    localStorage.setItem('userId', userId);
    localStorage.setItem('user', user);
}

function get_username() {
    let user = localStorage.getItem('user');
    return user
}

function get_user() {
    let userId = localStorage.getItem('userId');
    return userId
}

function set_token(token) {
    //set_token
    localStorage.setItem('token', token);

}

function get_echarts_data() {
    layui.$.ajax(
        {
            url: host + '/api/home_page',
            type: 'get',
            headers: {'token': get_token()},
            success: function (data) {
                console.log(data);
                return data;
            }
        }
    );
}

function remove_token() {
    //删除token
    localStorage.removeItem('token')
}

function logout() {
    remove_token();
    layui.$.ajax(
        {
            url: host + '/api/logout',
            type: 'post',
            headers: {'token': get_token()}
        }
    ); //调用退出接口
    top.window.location.href = 'starrysky/login.html';


}

//填充项目的下拉菜单,因为这个函数别的页面里面也用了，所以定义在这里，就不用多次定义了
function add_project(p) {
    projects = p;  //在这里定义了一个全局变量，就相当于在父页面定义了一个
    let str = '';
    for (let index in p) {
        let item = p[index]
        str += '<option value="' + item['id'] + '">' + item['name'] + '</option>'
    }
    layui.$('#project').append(str)
    layui.form.render('select')

}

//获取项目列表
function get_projects(call_back) {
    layui.$.ajax({
        url: host + '/api/project',
        data: {'limit': 100},
        headers: {'token': get_token()},
        type: 'get',
        success: function (data) {
            call_back(data.data)//调用回调函数，把项目列表传过去，不然的话，获取不到返回值
        }

    })

}


//动态添加input
function addParams(tab_id) {
    let timestamp = new Date().getTime(); //获取当前时间戳做key
    let input_key = `${tab_id}_key_${timestamp}`;
    let input_value = `${tab_id}_value_${timestamp}`;
    let css_class = tab_id === 'params' ? 'kv_div' : 'header_div'; //都给它加上一个class，用来区分是header还是参数
    let html = `<div class="layui-form-item ${css_class}" > <div class="layui-input-inline"><input type="text" name="${input_key}" required lay-verify="required"  placeholder="key" autocomplete="on" class="layui-input"> </div> <div class="layui-input-inline" style="margin-left: 10px"><input type="text" name="${input_value}" required lay-verify="required"  placeholder="value" autocomplete="on" class="layui-input"></div> <button type="button" class="layui-btn " lay-filter="add_input" onclick="addParams('${tab_id}')"  >增加</button> <button type="button" class="layui-btn-danger layui-btn" onclick="deleteParams('${tab_id}',this)">删除</button> </div>`

    document.getElementById(tab_id).insertAdjacentHTML('beforeEnd', html)
}


//动态删除input
function deleteParams(tab_id, ths) {
    let css_selector = tab_id === 'params' ? 'kv_div' : 'header_div';
    let element = document.getElementsByClassName(css_selector);
    let tab_obj = document.getElementById(tab_id);
    console.log(element.length);

    if (element.length === 1) {
        layer.alert('不能再删啦！');
    } else {
        tab_obj.removeChild(ths.parentElement)
    }
}


class FillInput {
    //填充接口参数和header
    fill(tab_id, data) {
        this.tab_id = tab_id;
        this.data = data;
        this.fillData = this.getFillData(); //获取编辑的数据
        this.css_selector = tab_id === 'params' ? 'kv_div' : 'header_div';

        if (this.data['is_json'] === true && this.tab_id === 'params') {
            //填充的时候判断参数是否是json
            this.setJsonStyle() //，展示json div
        } else {
            //不是json的，调用set k-v格式的函数
            this.setKvStyle() //
        }
    }


    getFillData() {
        //获取编辑的数据，根据传入的tab_id判断是请求头还是参数
        let data = this.tab_id === 'params' ? this.data['params'] : this.data['headers']
        return data
    }

    deleteDiv() {
        //删除默认的div
        layui.$(`.${this.css_selector}`).remove();
    }

    setJsonStyle() {
        layui.$('#json_div').css('display', 'block'); //默认json_div的display是none，改成block就显示出来了。
        layui.$('.kv_div').css('display', 'none'); //把kv_div显示出来。
    }

    setKvStyle() {
        let index = 0;//填充的时候每次的key不一样
        let key;
        if (this.fillData !== null && this.fillData !== '{}' && this.fillData !== '') {
            //判断是数据是否为空，不为空的话继续填充
            this.fillData = JSON.parse(this.fillData);
            this.deleteDiv(); //调用删除kv数据格式的方法，因为默认就有一条k-v的，填充的话，不需要那一条，所以删掉
            for (key in this.fillData) {
                let input_key = `${this.tab_id}_key_${index}`; //生成key_input的name
                let input_value = `${this.tab_id}_value_${index}`; //生成value_input的name
                let value = this.fillData[key]; //获取具体的vaule
                let html = `<div class="layui-form-item ${this.css_selector}" > <div class="layui-input-inline"><input type="text" name="${input_key}" value="${key}" required lay-verify="required"  placeholder="key" autocomplete="on" class="layui-input"> </div> <div class="layui-input-inline" style="margin-left: 10px"><input type="text" name="${input_value}" required lay-verify="required"  placeholder="value" value="${value}" autocomplete="on" class="layui-input"></div> <button type="button" class="layui-btn " lay-filter="add_input" onclick="addParams('${this.tab_id}')"  >增加</button> <button type="button" class="layui-btn-danger layui-btn" onclick="deleteParams('${this.tab_id}',this)">删除</button> </div>`
                document.getElementById(this.tab_id).insertAdjacentHTML('beforeEnd', html);
                index = index + 1; //数量每次+1
            }

        }
    }


}


//填充编辑用例时候的接口，就填充已经选择的一个接口
function case_interface_fill(interface_id, interface_name) {
    layui.$('#interface').empty();
    let str = '<option value="' + interface_id + '">' + interface_name + '</option>'
    layui.$('#interface').append(str)

}

// 填充依赖用例
function rely_case_fill(d) {
    let str = '';
    let case_list = d;
    for (let index in case_list) {
        let item = case_list[index];
        str += '<input type="checkbox" name="case" title="' + item['title'] + '" lay-skin="primary" value="' + item['id'] + '" checked>';
    }
    document.getElementById('rely_case').innerHTML = str;
    layui.form.render('checkbox')

}

//组装提交的参数，把它变成一个字典
function get_submit_data(data) {

    let default_params = {}
    let default_headers = {}

    for (key in data) {

        // {'headers_key_0': 'username','headers_value_0':'abc123','headers_key_1':'password','headers_value_1':'aA123456'}

        if (key.indexOf('headers_key') !== -1) {
            //1、key = headers_key_0
            //2、value_key经过替换后找到， 把上面的headers_key替换成headers_value就知道了value的key是什么
            //3、判断key是不是为空，为空的话，就直接删掉
            //4、有key和value了之后，就加到字典里面
            //5、最后删除原来的那些key

            let value_key = key.replace('headers_key', 'headers_value')
            //先判断是不是空，如果是空就不要了
            if (data[key] != '') {
                let header_key = data[key]
                let header_value = data[value_key]
                default_headers[header_key] = header_value

            }

            delete data[key]
            delete data[value_key]

        } else if (key.indexOf('params_key') !== -1) {

            let value_key = key.replace('params_key', 'params_value')

            if (data[key] != '') {
                let param_key = data[key]
                let param_value = data[value_key]
                default_params[param_key] = param_value

            }

            delete data[key]
            delete data[value_key]
        }
    }
    data['params'] = Object.keys(default_params).length === 0 ? null : JSON.stringify(default_params)  //如果是空字典，那么请求参数就null
    data['headers'] = Object.keys(default_headers).length === 0 ? null : JSON.stringify(default_headers)

    return data
}

function fill_interface_by_project(project_id) {
    layui.$.ajax({
        type: 'get',
        url: host + '/api/interface',
        data: {"project_id": project_id},
        headers: {'token': get_token()},
        success: function (data) {
            layui.$('#interface').empty();
            let str = '';
            let interface_list = data.data;
            for (let index in interface_list) {
                let item = interface_list[index]
                str += '<option value="' + item['id'] + '">' + item['name'] + '</option>'
            }
            layui.$('#interface').append(str)

            layui.form.render('select')


        }
    })

}

function fill_case_by_project(project_id,case_id=null) {
    layui.$.ajax({
        type: 'get',
        url: host + '/api/get_rely_case',
        data: {"project_id": project_id,'case_id':case_id},
        headers: {'token': get_token()},
        success: function (data) {
            let str = '';
            let case_list = data.data;
            for (let index in case_list) {
                let item = case_list[index];
                str += '<input type="checkbox" name="case" title="' + item['title'] + '" lay-skin="primary" value="' + item['id'] + '">';
            }
            document.getElementById('rely_case').innerHTML = str;
            layui.form.render('checkbox')
        }
    })
}


//获取url里面参数
function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    console.log(query);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return (undefined);
}

