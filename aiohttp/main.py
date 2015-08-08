import asyncio
from aiohttp import web

# pypy does not have ujson
try:
    import ujson as json
except ImportError:
    import json


@asyncio.coroutine
def handle(request):
    data = {}
    keys = ["key%s" % i for i in range(1, 11)]
    for key in keys:
        data[key] = request.GET.get(key, "")
        assert isinstance(data[key], (str, bytes))
    resp = {"status_code": 200, "status_txt": "OK", "data": data}
    text = json.dumps(resp)
    return web.Response(body=text.encode('utf-8'))


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', handle)

    srv = yield from loop.create_server(app.make_handler(),
                                        '127.0.0.1', 8080)
    print("Server started at http://127.0.0.1:8080")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
