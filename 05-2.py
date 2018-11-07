from flask import  Flask, make_response

app = Flask(__name__)


with app.test_request_context():
    resp = make_response('', 400)
    print(resp)
    print(type(resp))