from flask import Flask, jsonify
from flask.views import MethodView
app = Flask(__name__)

class UserApi(MethodView):
    def get(self):
        return jsonify({
            'username': '足下',
            'avatar': 'http://www.cqzuxia.com/static/images/newindex/logo.png'
        })
    def post(self):
        return 'UNSUPPORTED!'

app.add_url_rule('/user', view_func=UserApi.as_view('userview'))


if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)