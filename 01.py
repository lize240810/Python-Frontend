from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    a = 1 / 0
    return "Hello World!"

app.debug = True

# windows:
# set WERKZEUG_DEBUG_PIN=123-579-1-2-9-3-6-3
# linux/mac:
# export WERKZEUG_DEBUG_PIN=123-579-1-2-9-3-6-3
# python
import os
os.environ['WERKZEUG_DEBUG_PIN'] = '123-579-1-2-9-9-6-9'

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    # app.run(host='127.0.0.1')
    app.run(host='127.0.0.1', debug=True)
