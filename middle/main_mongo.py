import json
import os
import motor
import tornado
import tornado.web

client = motor.motor_tornado.MotorClient(os.environ['DB_HOST'], 27017)
db = client[os.environ['DB_NAME']]


class MainHandler(tornado.web.RequestHandler):
    async def post(self):
        db = self.settings['db']

        result = await db.devices.insert_one(json.loads(self.request.body.decode('utf-8')))
        self.write(result.inserted_id)


application = tornado.web.Application([
    (r'/', MainHandler)
], debug=False, db=db)

application.listen(8888)
tornado.ioloop.IOLoop.current().start()
