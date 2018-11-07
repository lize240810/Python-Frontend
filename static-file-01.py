from flask import Flask, send_from_directory

import os

# app = Flask(__name__)
app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/static'
)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)