from flask import Flask, url_for, abort, redirect

app = Flask(__name__)

@app.route('/30x')
def view_30x():
    return 'hahah'

@app.route('/301')
def index_301():
    # 301： 永久重定向
    location = url_for('view_30x')
    print(location)
    return redirect(location, 301)

@app.route('/302')
def index_302():
    # 302： 零时重定向
    location = url_for('view_30x')
    print(location)
    return redirect(location, 302)

@app.route('/baidu')
def index_baidu():
    location = 'https://blog.gsw945.com/'
    return redirect(location)

@app.route('/4<int:error>')
def index_40x(error):
    print(error)
    # 400, 401, 403, 404
    abort(400 + error)

@app.route('/5<int:error>')
def index_50x(error):
    print(error)
    # 500, 502, 503, 504
    abort(500 + error)

if __name__ == '__main__':
    app.run(debug=True)