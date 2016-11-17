import falcon
import mongoengine as mongo

import settings
from middlewares.jsonify import JsonifyMiddleware


api = falcon.API(middleware=[
    JsonifyMiddleware(),
])

mongo.connect(
    settings.MONGO['DATABASE'],
    host = settings.MONGO['HOST'],
    port = settings.MONGO['PORT'],
    username = settings.MONGO['USERNAME'],
    password = settings.MONGO['PASSWORD']
)
