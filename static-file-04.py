from flask import Flask, send_from_directory

import os

app = Flask(__name__)
FOLDER = os.path.dirname(os.path.abspath(__file__))

@app.route('/<path:filename>')
def static_overwrite(filename):
    static_folder = FOLDER
    return send_from_directory(static_folder, filename)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)