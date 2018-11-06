import os
os.environ['WERKZEUG_DEBUG_PIN'] = '123-456-543-21'

from urllib import parse
from werkzeug.routing import BaseConverter

class ListConverter(BaseConverter):
    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        # urlencode与unquote: https://blog.csdn.net/a359680405/article/details/44857359
        self.separator = parse.unquote(separator)
    def to_python(self, value):
        print(value)
        return value.split(self.separator)
    def to_url(self, values):
        print(values)
        return self.separator.join(
            BaseConverter.to_url(value) for value in values
        )


from flask import Flask
app = Flask(__name__)

app.url_map.converters['list'] = ListConverter

@app.route('/r/<list:subreddits>')
def subreddit_home(subreddits):
    posts = []
    for subreddit in subreddits:
        print(subreddit)
        posts.append(subreddit)
    return 'data: ' + '、'.join(posts)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)