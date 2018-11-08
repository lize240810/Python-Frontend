from flask import Blueprint

bp = Blueprint('file', __name__, url_prefix='/file')

@bp.route('/')
def index():
    return "文件首页"

@bp.route('/upload')
def upload():
    return "上传"

@bp.route('/download')
def download():
    return "下载"