from flask import Flask
from flask.views import View

try:
    from flask_debugtoolbar import DebugToolbarExtension
except ImportError:
    import os
    os.system('pip install flask-debugtoolbar')
    from flask_debugtoolbar import DebugToolbarExtension

class IndexView(View):
    """Index视图"""
    def dispatch_request(self):
        return '<body>视图函数返回的方法</body>'


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '<replace with a secret key>'
DebugToolbarExtension(app)


app.add_url_rule('/hello', view_func=IndexView.as_view('viwhello'))

@app.route('/world')
def view_word():
    return '<body>world</body>'

if __name__ == '__main__':
    app.run()