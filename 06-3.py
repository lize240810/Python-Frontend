'''
[1.0.2:可插拨视图]: https://dormousehole.readthedocs.io/en/latest/views.html
[0.10.1:即插视图]: http://docs.jinkan.org/docs/flask/views.html
[1.0:Pluggable Views]: http://flask.pocoo.org/docs/1.0/views/
'''
from flask import Flask, request
from flask.views import View


class IndexView(View):
    """Index视图"""
    methods = ['GET', 'POST', 'DELETE']

    def dispatch_request(self):
        return __class__.__name__ + ': 访问方法是：' + request.method


app = Flask(__name__)

app.config['DEBUG'] = True


app.add_url_rule('/hello', view_func=IndexView.as_view('viwhello'))

@app.route('/world', methods=['GET', 'POST'])
def view_word():
    return 'view_word: 访问方法: ' + request.method

if __name__ == '__main__':
    app.run()