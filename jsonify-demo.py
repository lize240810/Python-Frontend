from flask import Flask


app = Flask(__name__)

data = {
    'username': '足下',
    'avatar': 'http://www.cqzuxia.com/static/images/newindex/logo.png'
}

@app.route('/jsonify')
def view_jsonify():
    global data

    from flask import jsonify
    resp = jsonify(data)

    return resp

@app.route('/json-dumps')
def view_json_dumps():
    global data
    
    import json
    data_str = json.dumps(data)

    from flask import make_response
    resp = make_response(data_str)
    resp.headers['Content-Type'] = 'application/json'

    return resp

if __name__ == '__main__':
    app.run(debug=True)