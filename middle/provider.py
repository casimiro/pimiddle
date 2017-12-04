import tornado
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    async def post(self):
        self.write('{"insertion": "ok"}')


application = tornado.web.Application([
    (r'/', MainHandler)
], debug=False)

application.listen(8888)
tornado.ioloop.IOLoop.current().start()
