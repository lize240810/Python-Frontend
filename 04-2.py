from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__)
app.config['DEBUG'] = True
# app.debug = True

@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    '''
    # 测试代码：
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    requests.get('http://127.0.0.1:9000/people/?name=666', headers=headers).text
    '''
    user_agent = request.headers.get('User-Agent')
    return 'Name: {0}; UA: {1}'.format(name, user_agent)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        '''
        # 测试代码：
        import requests
        requests.post('http://127.0.0.1:9000/login/', data={'use＿id': '999'}).text
        '''
        user_id = request.form.get('use＿id')
        return 'User: {} login'.format(user_id)
    else:
        return '打开登录页面'


@app.route('/secret/')
def secret():
    # return abort(401)
    abort(401)
    print('有本事执行我呀')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=9000,
        debug=app.debug)