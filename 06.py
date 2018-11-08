from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__, template_folder='./templates')

class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError()
    def render_template(self, context):
        return render_template(self.get_template_name(), **context)
    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED!'
        context = {'user': self.get_user()}
        return self.render_template(context)
    def get_user(self):
        raise NotImplementedError()

class UserView(BaseView):
    def get_template_name(self):
        return 'users.html'
    def get_user(self):
        return {
            'username': 'zuxia',
            'avatar': 'http://www.cqzuxia.com/static/images/newindex/logo.png'
        }

app.add_url_rule('/user', view_func=UserView.as_view('userview'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)