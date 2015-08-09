# pypy does not have ujson
try:
    import ujson as json
except ImportError:
    import json

# wsgiref only works in py2 and pypy
dev_server = False
try:
    from wsgiref import simple_server
    dev_server = True
except ImportError:
    pass

import falcon


class QueryParamResource(object):
    def on_get(self, req, resp):
        data = {}
        keys = ["key%s" % i for i in range(1, 11)]
        for key in keys:
            data[key] = req.get_param(key)
        assert isinstance(data[key], (str, bytes))
        r = {"status_code": 200, "status_txt": "OK", "data": data}
        resp_json = json.dumps(r)
        resp.set_header('Content-Type', 'application/json; charset=utf-8')
        resp.body = resp_json

application = falcon.API()
query_handler = QueryParamResource()
application.add_route('/', query_handler)

if __name__ == '__main__' and dev_server:
    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()
