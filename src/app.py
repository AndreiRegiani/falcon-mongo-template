import falcon
import falcon_jsonify
import mongoengine as mongo

import settings


api = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=settings.DEBUG),
])

mongo.connect(
    settings.MONGO['DATABASE'],
    host = settings.MONGO['HOST'],
    port = settings.MONGO['PORT'],
    username = settings.MONGO['USERNAME'],
    password = settings.MONGO['PASSWORD']
)
