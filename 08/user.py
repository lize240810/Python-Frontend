from flask import Blueprint

# 指定路径前置 url_prefix，优先级比 register_blueprint() 低
bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def index():
    return "用户首页-一般会显示用户信息啥的"

@bp.route('/login')
def login():
    return "登录页"

@bp.route('/logout')
def logout():
    return "登出（注销）页"