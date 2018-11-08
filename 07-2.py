from flask import Flask, jsonify
from flask.views import MethodView
from flask import request, abort
# https://docs.python.org/3/library/functools.html#functools.wraps
from functools import wraps


app = Flask(__name__)

class UserApi(MethodView):
    def get(self):
        return jsonify({
            'username': '足下',
            'avatar': 'http://www.cqzuxia.com/static/images/newindex/logo.png'
            })
    def post(self):
        return 'UNSUPPORTED!'

def user_required(f):
    # wraps可以保护被装饰的函数的名称不被改变
    @wraps(f)
    def decorator(*args, **kwargs):
        # 用户名列表
        names = ['ruirui', 'python', 'cn', 'zh', 'hans', 'ubuntu']
        # 从请求参数中获取用户名
        name = request.values.get('name')
        # 将name转成小写，如果name有值的话
        if bool(name):
            name = name.lower()
        else:
            # 如果没有提供name ，抛出400错误
            abort(400)
        if name not in names:
            # 如果给定的name不在用户名列表中，抛出403错误
            abort(403)
        # 执行被装饰的函数
        return f(*args, **kwargs)
    return decorator

class VV(MethodView):
    def get():
        return 'get'
        

view1 = user_required(UserApi.as_view('userview'))
print(view1.__name__)
app.add_url_rule('/user', view_func=view1)

view2 = user_required(VV.as_view('vv'))
print(view2.__name__)
app.add_url_rule('/vv', view_func=view2)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)