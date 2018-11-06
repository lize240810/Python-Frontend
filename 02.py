from flask import Flask, request
app = Flask(__name__)


@app.route('/age/1')
@app.route('/age/2')
@app.route('/age/3')
@app.route('/age/4')
@app.route('/age/5')
@app.route('/age/6')
@app.route('/age/7')
@app.route('/age/8')
def age():
    # 请求路径
    path = request.path
    id = path.split('/')[-1]
    return 'Age: {0}'.format(id)

@app.route('/item')
def item2():
    name = request.values.get('name')
    return 'Name: {0}'.format(name)

@app.route('/path/<path:id>')
def view_path(id):
    print(type(id))
    return 'Item: {0}'.format(id)

@app.route('/string/<string:id>')
def view_string(id):
    print(type(id))
    return 'Item: {0}'.format(id)

@app.route('/int/<int:id>')
def view_int(id):
    print(type(id))
    return 'Item: {0}'.format(id)

@app.route('/float/<float:id>')
def view_float(id):
    print(type(id))
    return 'Item: {0}'.format(id)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)