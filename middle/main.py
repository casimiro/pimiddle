import os
import tornado
import tornado.web
from tornado.httpclient import AsyncHTTPClient

UPSTREAM_HOST = os.environ['UPSTREAM_HOST']


class MainHandler(tornado.web.RequestHandler):
    async def post(self):
        http_client = AsyncHTTPClient()
        url = 'http://%s:8888/' % (UPSTREAM_HOST)
        result = await http_client.fetch(url, method='POST', body=self.request.body.decode('utf-8'))
        self.write(result.body.decode())


application = tornado.web.Application([
    (r'/', MainHandler)
], debug=False)

application.listen(8888)
tornado.ioloop.IOLoop.current().start()
