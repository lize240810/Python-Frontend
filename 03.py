from flask import Flask, url_for

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return ''

with app.test_request_context():
    # app.test_request_context() 模拟一个请求上下文环境（模拟一个请求来了）
    print(url_for('index', name='666'))
    print(url_for('index', name='666', hello='world'))
    # print(url_for('index', hello='world')) # 缺少name会报错，url参数中的name是必须的
    print(url_for('index', name='666', hello='world', _external=True)) # 生成外部地址
    # 外部地址，是带有域的完整URL
    # 默认是内部地址（URL去掉域部分）
    # 域 = 协议 + 主机(域名) + 端口
    print(url_for('index', name='666', hello='world', course='Python程序设计'))
