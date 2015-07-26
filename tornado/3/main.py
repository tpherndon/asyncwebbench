from tornado import gen
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        data = {}
        keys = ["key%s" % i for i in range(1, 11)]
        for key in keys:
            data[key] = self.get_query_argument(key)
            assert isinstance(data[key], (str, bytes))
        resp = {"status_code": 200, "status_txt": "OK", "data": data}
        self.write(resp)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
