from flask import Blueprint


# url_prefix 默认为 '', 所以可以省略
# bp = Blueprint('index', __name__, url_prefix='')
bp = Blueprint('index', __name__)

@bp.route('/')
def view_index():
    return "首页"