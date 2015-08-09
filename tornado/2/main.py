from tornado import gen
import tornado.ioloop
import tornado.options
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        data = {}
        keys = ["key%s" % i for i in xrange(1, 11)]
        for key in keys:
            data[key] = self.get_query_argument(key)
            assert isinstance(data[key], (str, unicode))
        resp = {"status_code": 200, "status_txt": "OK", "data": data}
        self.write(resp)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    tornado.options.define('port', type=int, default=9000, help='Listen port')
    tornado.options.parse_command_line()
    application.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
