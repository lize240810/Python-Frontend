# refer: https://stackoverflow.com/questions/12162634/where-do-i-define-the-domain-to-be-used-by-url-for-in-flask
from flask import Flask, url_for

import os

app = Flask(__name__)
# http://flask.pocoo.org/docs/1.0/config/#SERVER_NAME
app.config['SERVER_NAME'] = 'demo.gsw945.com:5000'
# http://flask.pocoo.org/docs/1.0/config/#PREFERRED_URL_SCHEME
app.config['PREFERRED_URL_SCHEME'] = 'http'

@app.route('/hello')
def view_hello():
    return 'VF:hello'

with app.test_request_context():
    print(url_for('view_hello', _external=True))