import json
import os
import motor
import tornado
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    async def post(self):
        db = self.settings['db']

        result = await db.devices.insert_one(json.loads(self.request.body.decode('utf-8')))
        self.write(str(result.inserted_id))


if __name__ == "__main__":
    client = motor.motor_tornado.MotorClient(os.environ['DB_HOST'], 27017)
    db = client[os.environ['DB_NAME']]

    app = tornado.web.Application([
        (r'/', MainHandler)
    ],
    debug=False,
    db=db)

    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    tornado.ioloop.IOLoop.instance().start()
