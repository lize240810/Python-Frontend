from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['re'] = RegexConverter

@app.route(r'/<re("[1-7]{1}|一|二|三"):week>/<re("[^\/]*"):name>/')
def example(week, name):
    # week = args[0]
    msg1 = "今天是 星期{0}".format("日" if week == "7" else week)
    msg2 = name
    return '<br />'.join((msg1, msg2))

if __name__ == '__main__':
    app.run(debug=True)
