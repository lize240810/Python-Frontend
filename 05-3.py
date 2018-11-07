from flask import Flask, make_response, abort

app = Flask(__name__)

# 重写404错误的输出
@app.errorhandler(404)
def not_found(error):
    return '''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>404 Not Found</title>
    <h1>Not Found Found Found</h1>
    <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
    ''', 404

# 重写401错误的输出
@app.errorhandler(401)
def bad_request(error):
    # 创建一个响应对象
    resp = make_response('错误的请求', 401)
    # 设置响应头
    resp.headers['X-Name'] = 'zhangsan'
    return resp

# 重写500错误的输出
@app.errorhandler(500)
def bad_request(error):
    # error.get_description()
    # 创建一个响应对象
    resp = make_response('错误的请求', 500)
    # 下面的是调试代码，ipdb需要用pip安装
    # import ipdb as pdb; pdb.set_trace()
    import traceback
    # 设置响应头
    # traceback.format_exc() 获取异常堆栈信息
    # 每一个HTTP头不能换行，所以需要去掉头中的换行(\n)
    resp.headers['X-Error'] = traceback.format_exc().replace('\n', '<br />')
    return resp

@app.route('/40<int:ccc>')
def view_40x(ccc):
    abort(400 + ccc)

@app.route('/500')
def view_500():
    abort(500)

@app.route('/dict')
def view_dict():
    return {
        'name': 'mingzi',
        '说明': '视图函数不能返回字典，这里会报错哟'
    }

if __name__ == '__main__':
    print('*' * 66)
    print('请访问以下地址:')
    print('http://127.0.0.1:9000/401')
    print('http://127.0.0.1:9000/404')
    print('*' * 66)
    app.run(host='0.0.0.0', port=9000, debug=True)