from flask import Flask
from flask import make_response
from flask import request

# pypy does not have ujson
try:
    import ujson as json
except ImportError:
    import json

app = Flask(__name__)

@app.route('/')
def json_echo():
    data = {}
    keys = ["key%s" % i for i in xrange(1, 11)]
    for key in keys:
        data[key] = request.args[key]
        assert isinstance(data[key], (str, unicode))
    resp = {"status_code": 200, "status_txt": "OK", "data": data}
    resp_json = json.dumps(resp)
    response = make_response(resp_json)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run()
