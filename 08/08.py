from flask import Flask

app = Flask(__name__)

import home
app.register_blueprint(home.bp)

import user
app.register_blueprint(user.bp)

import file
# 注册蓝图时，指定url_prefix, 这里指定的优先级高
app.register_blueprint(file.bp, url_prefix='/fff')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)